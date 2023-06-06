# Задача 30: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.
# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input,
# в одну строку, вам понадобится распаковка и Comprehension или map

# Базовое решение:

# def arithmetic_progression(a1: int, d: int, n: int) -> list:
#     a_n = a1 + (n - 1) * d
#     new_list = []
#     for i in range(a1, a_n + 1, d):
#         new_list.append(i)
#     return new_list

# print(arithmetic_progression(7, 2, 5))
# print(arithmetic_progression(2, 3, 12))

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# def arithmetic_progression(a1: int, d: int, n: int) -> list:
#     a_n = a1 + (n - 1) * d
#     res_list = [i for i in range(a1, a_n + 1, d)]
#     return res_list

# print(arithmetic_progression(7, 2, 5))
# print(arithmetic_progression(2, 3, 12))

# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input,
# в одну строку, вам понадобится распаковка и Comprehension или map

a1, d, n = map(int, input().split())

def arithmetic_progression(a1: int, d: int, n: int) -> list:
    a_n = a1 + (n - 1) * d
    res_list = [i for i in range(a1, a_n + 1, d)]
    return res_list

print(arithmetic_progression(a1, d, n))