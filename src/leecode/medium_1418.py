from collections import defaultdict
from datetime import datetime
from typing import List

'''
tag: ^1418 ^medium ^hash-table
name: ^()
'''


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_dic = {}
        food_set = set()

        for lst in orders:
            food_dic = table_dic.get(int(lst[1]), defaultdict(int))
            food_dic[lst[2]] += 1
            table_dic[int(lst[1])] = food_dic
            food_set.add(lst[2])

        res = []
        # head_column=["Table"]
        head_column = sorted(food_set)
        res.append(head_column)

        table_lst = sorted(table_dic.keys())
        for table_id in table_lst:
            row = [str(table_id)]
            for food in head_column:
                row.append(str(table_dic[table_id][food]))
            res.append(row)
        res[0].insert(0, "Table")
        return res


orders = [["David", "3", "Ceviche"],
          ["Corina", "10", "Beef Burrito"],
          ["David", "3", "Fried Chicken"],
          ["Carla", "5", "Water"],
          ["Carla", "5", "Ceviche"],
          ["Rous", "3", "Ceviche"]]

t1 = datetime.now()
s = Solution()
print(s.displayTable(orders))
t2 = datetime.now()
print(t2 - t1)
