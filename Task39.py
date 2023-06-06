# Задача 39: Даны два списка чисел. Требуется вывести те элементы первого списка, 
# которых нет во втором списке.
# Создайте функцию.
# Аргументы: два списка целых чисел
# Возвращает: список элементов (смотри условие)
# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]
# [*] Усложнение. Элементы необходимо возвращать в том порядке, 
# в котором они находятся в первом списке, с учетом повторений
# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]

# list_1 = [3, 1, 3, 4, 2, 4, 12]
# list_2 = [4, 15, 43, 1, 15, 1]
# def difference_elements(list_n: list, list_m: list) -> list:
#     set_list_n = set(list_n)
#     set_list_m = set(list_m)
#     return list(set_list_n.difference(set_list_m))
# print(difference_elements(list_1, list_2))

# [*] Усложнение.

list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
def difference_elements(list_n: list, list_m: list) -> list:
    set_list_m = set(list_m)
    new_list = []
    for i in list_n:
        if i not in set_list_m:
            new_list.append(i)
    return new_list
print(difference_elements(list_1, list_2))
