# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list = []

for _ in range (random.randint(1,10)):
    list.insert(_, round(random.uniform(1,10),2))
print(f'Сгенерированный массив: {list}')

max = 0
for _ in range(len(list)):
    if list[_] - int(list[_]) > max:
        max = list[_] - int(list[_])

min = 1
for _ in range(len(list)):
    if list[_] - int(list[_]) < min:
        min = list[_] - int(list[_])

print(f'Разница между наибольшей и наименьшей дробными частями: {int((max - min)*100)/100}')
