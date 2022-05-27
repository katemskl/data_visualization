from die import Die

import pygal

# Создание кубиков D6 & D10

die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(50000):
    results.append(die_1.roll() + die_2.roll())

# Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

# Визуализация результатов
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10 50.000 times'
hist.x_labels = [str(x) for x in range(17)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice2_visual.svg')