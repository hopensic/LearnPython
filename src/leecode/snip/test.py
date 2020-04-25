import operator
from itertools import accumulate

# data = [[1, 2, 3],
#         [4, 5, 6],
#         [1, 1, 1]
#         ]
data = [[1, -1],
        [-1, 1]
        ]

for lst in data:
    for i, x in enumerate(accumulate(lst, operator.add)):
        lst[i] = x
for j in range(len(data[0])):
    for i, x in enumerate(accumulate([data[i][j] for i in range(len(data))], operator.add)):
        data[i][j] = x

print(data)
