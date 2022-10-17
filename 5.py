# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введите число для последовательности фибоначи: '))
fibonachi_list = [0,1]
negafibonachi_list = [0,1]
def Find_fibonachi (num_max, count, list):
    list.append(list[count] + list[count+1])
    if (num_max - 2) > count:
        Find_fibonachi (num_max, count+1, list)
    
    return list

def Find_negafibonachi (num_max, count, list):
    list.append(list[count] - list [count+1])
    if (num_max - 2) > count:
        Find_negafibonachi (num_max, count+1, list)
    
    return list

Find_fibonachi(num,0, fibonachi_list)
Find_negafibonachi(num,0, negafibonachi_list)

result_list = []
for _ in range(len(negafibonachi_list) + len(fibonachi_list) - 1):
    if _ < len(negafibonachi_list):
        result_list.append(negafibonachi_list[(-_)-1])
    if len(negafibonachi_list) <= _:
        result_list.append(negafibonachi_list[(_ - (len(fibonachi_list)-1))]) 

print(f'Последовательность негафибоначчи и фибоначчи: {result_list}')