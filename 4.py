# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Введите число для перевода в двоичную систему исчесления: "))
output = num
result = ''
while num > 0:
    if num % 2 != 0:
        result = result + '0'
    else:
        result = result + '1'
    num = int(num/2)

print(f'{output} в двоичной системе равняется {result}.')
