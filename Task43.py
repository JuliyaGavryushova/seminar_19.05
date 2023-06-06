# Задача 43: Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару,
# которую необходимо посчитать.
# Напишите функцию
# Аргументы: список целых чисел
# Возвращает: кол-во пар
# Примеры/Тесты:
# <function_name>([1, 2, 3, 2, 3]) -> 2
# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

def pair_numbers(list_n: list) -> int:
    count = 0
    for i in range(len(list_n)):
        for j in range(i + 1, len(list_n)):
            if list_n[i] == list_n[j]:
                count += 1
    return count

print(pair_numbers([1, 2, 3, 2, 3]))
print(pair_numbers([1, 2, 3, 2, 3, 3, 2, 4]))

# def pair_numbers(list_n: list) -> int:
#     count = 0
#     for i in range(len(list_n)):
#         count += list_n[i + 1:].count(list_n[i])
#     return count

# print(pair_numbers([1, 2, 3, 2, 3]))
# print(pair_numbers([1, 2, 3, 2, 3, 3, 2, 4]))