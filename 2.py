# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

list = []
for _ in range(random.randint(1,10)):
    list.insert(_, random.randint(1,10))
print(f'Сгенерированный массив: {list}')
list_result = []

for _ in range(round(len(list)/2)):
    list_result.append(list[_] * list[(-_-1)])

print(list_result)