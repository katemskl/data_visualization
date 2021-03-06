import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму

keep_running = 'y'

while True:
    rw = RandomWalk(100)
    rw.fill_walk()
    points_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Blues, edgecolors='none', s=10)

    # Выделение первой и последней точек
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Удаление осей
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running.lower() == 'n':
        break


