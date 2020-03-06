from collections import defaultdict


class ProductOfNumbers:

    def __init__(self):
        self.dic_lst = []  # 字典数组
        self.lst = []  # 存储每次追加的整数

    def add(self, num: int) -> None:
        self.lst.append(num)
        # 每次新增时，copy字典数组中最后一个字典，并且将新增的整数存入该字典中
        if len(self.dic_lst) == 0:
            dic = defaultdict(int)
            dic[num] += 1
            self.dic_lst.append(dic)
        else:
            dic = self.dic_lst[-1].copy()
            dic[num] += 1
            self.dic_lst.append(dic)

    def getProduct(self, k: int) -> int:
        # 获取字典中所有数的乘积
        def get_dic_product(dic_tmp):
            if dic_tmp[0] > 0:
                return 0
            num = 1
            for k, v in dic_tmp.items():
                if v <= 0:
                    continue
                num *= k ** dic_tmp[k]
            return num

        # 获取字典数组中尾部的字典，其中存储了当前所有的整数及出现的次数
        total_dic = self.dic_lst[-1].copy()
        if k == 1:
            return self.lst[-1]
        if k == len(self.lst):
            return get_dic_product(self.dic_lst[-1])

        # 获取字典数组中倒数第k-1个字典，其中存储数了当前除去倒数k个整数的所有整数及出现次数
        pre_dic = self.dic_lst[len(self.dic_lst) - k - 1]
        for k, v in pre_dic.items():
            total_dic[k] -= v
        return get_dic_product(total_dic)


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_1 = obj.getProduct(2)
param_2 = obj.getProduct(3)

print(param_1)
print(param_2)
