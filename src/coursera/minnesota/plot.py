import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('eval-results.csv')
df = df.rename(columns=lambda x: x.replace('.', '_'))
df.head()


baselines = df[df.NNbrs.isnull()]


const_rmse = baselines.pivot(index='Partition', columns='Algorithm', values='RMSE_ByUser')
const_rmse.plot(kind='box')

baselines.pivot(index='Partition', columns='Algorithm', values='TopN_nDCG').plot(kind='box')
baselines.pivot(index='Partition', columns='Algorithm', values='Predict_nDCG').plot(kind='box')

