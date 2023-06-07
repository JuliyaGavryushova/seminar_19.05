# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

# Базовое решение:

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# def indexes_elements(list_n: list, dist1: int, dist2: int) -> list:
#     new_list = []
#     for i in range(len(list_n)):
#         if list_n[i] in range(dist1, dist2 + 1):
#             new_list.append(i)
#     return new_list

# print(indexes_elements(list_1, 2, 10))
# print(indexes_elements(list_1, 2, 9))
# print(indexes_elements(list_1, 0, 6))

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# def indexes_elements(list_n: list, dist1: int, dist2: int) -> list:
#     new_list = [i for i in range(len(list_n)) if list_n[i] in range(dist1, dist2 + 1)]
#     return new_list

# print(indexes_elements(list_1, 2, 10))
# print(indexes_elements(list_1, 2, 9))
# print(indexes_elements(list_1, 0, 6))

# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def indexes_elements(list_n: list, dist1: int, dist2: int) -> list:
    new_list = []
    for i in range(len(list_n)):
        if list_n[i] in range(dist1, dist2 + 1):
            pair = (i, list_n[i],)
            new_list.append(pair)
    return new_list

print(indexes_elements(list_1, 2, 10))
print(indexes_elements(list_1, 2, 9))
print(indexes_elements(list_1, 0, 6))