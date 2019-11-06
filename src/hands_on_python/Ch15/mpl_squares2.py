import matplotlib.pyplot as plt

from hands_on_python.common.commons import ps

squares = [1, 4, 9, 16, 25]

# 设置标题，给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.plot(squares, linewidth=5)
plt.show()
ps()
