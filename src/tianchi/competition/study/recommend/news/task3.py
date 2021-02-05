import pandas as pd
import numpy as np
from tqdm import tqdm
from collections import defaultdict
import os, math, warnings, math, pickle
from tqdm import tqdm
import collections
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

# from deepctr.feature_column import SparseFeat, VarLenSparseFeat
# from sklearn.preprocessing import LabelEncoder
#
# from deepmatch.models import *
# from deepmatch.utils import sampledsoftmaxloss

warnings.filterwarnings('ignore')

data_path = 'e:/tmp/'
save_path = 'e:/tmp/'
# 做召回评估的一个标志, 如果不进行评估就是直接使用全量数据进行召回
metric_recall = False


# debug模式： 从训练集中划出一部分数据来调试代码
def get_all_click_sample(data_path, sample_nums=3):
    """
        训练集中采样一部分数据调试
        data_path: 原数据的存储路径
        sample_nums: 采样数目（这里由于机器的内存限制，可以采样用户做）
    """
    all_click = pd.read_csv(data_path + 'train_click_log.csv')
    all_user_ids = all_click.user_id.unique()

    sample_user_ids = np.random.choice(all_user_ids, size=sample_nums, replace=False)
    all_click = all_click[all_click['user_id'].isin(sample_user_ids)]

    all_click = all_click.drop_duplicates((['user_id', 'click_article_id', 'click_timestamp']))
    return all_click


# 读取文章的基本属性
def get_item_info_df(data_path):
    item_info_df = pd.read_csv(data_path + 'articles.csv')

    # 为了方便与训练集中的click_article_id拼接，需要把article_id修改成click_article_id
    item_info_df = item_info_df.rename(columns={'article_id': 'click_article_id'})

    return item_info_df


# 读取文章的Embedding数据
def get_item_emb_dict(data_path):
    item_emb_df = pd.read_csv(data_path + 'articles_emb.csv')

    item_emb_cols = [x for x in item_emb_df.columns if 'emb' in x]
    item_emb_np = np.ascontiguousarray(item_emb_df[item_emb_cols])
    # 进行归一化
    item_emb_np = item_emb_np / np.linalg.norm(item_emb_np, axis=1, keepdims=True)

    item_emb_dict = dict(zip(item_emb_df['article_id'], item_emb_np))
    pickle.dump(item_emb_dict, open(save_path + 'item_content_emb.pkl', 'wb'))

    return item_emb_dict


max_min_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))

# a = pd.Series([1, 2, 3, 4])
# b = pd.Series([1, 2, 3])
#
# c = [a, b].apply(max_min_scaler)

# 采样数据
all_click_df = get_all_click_sample(data_path)

# 对时间戳进行归一化,用于在关联规则的时候计算权重
all_click_df['click_timestamp'] = all_click_df[['click_timestamp']].apply(max_min_scaler)

item_info_df = get_item_info_df(data_path)

item_emb_dict = get_item_emb_dict(data_path)
