# Задача 11: Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является.
# Т.е. выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Примеры/Тесты:
# 5 -> в ряду Фибоначчи 5 имеет порядковый номер 6
# 6765 -> в в ряду Фибоначчи 6765 имеет порядковый номер 21
# 6766 -> -1
# Примечание: Вы можете решить эту задачу, используя формулу чисел Фибоначчи или итеративно.

n = int(input("Введите натуральное число: "))
first_num = 0
second_num = 1
third_num = first_num + second_num
count = 3
while n > third_num:
    first_num = second_num
    second_num = third_num
    third_num = first_num + second_num
    count += 1
if third_num == n:
    print(count)
else: 
    print(-1)