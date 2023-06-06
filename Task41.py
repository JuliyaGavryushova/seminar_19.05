# Задача 41: Дан список, целых чисел.
# Напишите функцию, которая определит те элементы списка, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Функция
# Аргументы: список целых чисел
# Возвращает: список элементов (смотри условие)
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 5]) -> [5]
# <function_name>([1, 5, 1, 6, 1]) -> [5,6]
# <function_name>([7, 5, 1, 6, 8]) -> [8]
# <function_name>([8, 1, 5, 4, 5]) -> [8,5]

# list_1 = [8, 1, 5, 4, 5]
# def neighboring_elements_smaller(list_n: list) -> list:
#     new_list = []
#     for i in range(len(list_n)):
#         if i == 0:
#             if list_n[i] > list_n[i + 1] and list_n[i] > list_n[len(list_1) - 1]:
#                 new_list.append(list_n[i])
#         elif i == len(list_1) - 1:
#             if list_n[i] > list_n[i - 1] and list_n[i] > list_n[0]:
#                 new_list.append(list_n[i])
#         else:
#             if list_n[i] > list_n[i - 1] and list_n[i] > list_n[i + 1]:
#                 new_list.append(list_n[i])
#     return new_list
# print(neighboring_elements_smaller(list_1))

def neighboring_elements_smaller(list_n: list) -> list:
    new_list = []
    for i in range(len(list_n) - 1):
        if list_n[i] > list_n[i - 1] and list_n[i] > list_n[i + 1]:
            new_list.append(list_n[i])
    i = len(list_n) - 1
    if list_n[i] > list_n[i - 1] and list_n[i] > list_n[0]:
        new_list.append(list_n[i])
    return new_list

print(neighboring_elements_smaller([1, 3, 3, 3, 5]))
print(neighboring_elements_smaller([1, 5, 1, 6, 1]))
print(neighboring_elements_smaller([7, 5, 1, 6, 8]))
print(neighboring_elements_smaller([8, 1, 5, 4, 5]))