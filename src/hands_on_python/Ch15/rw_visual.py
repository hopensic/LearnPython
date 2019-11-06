import matplotlib.pyplot as plt

from hands_on_python.Ch15.random_walk import RandomWalk

rw =RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()