import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму

rw = RandomWalk(100)
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=10)
plt.show()
