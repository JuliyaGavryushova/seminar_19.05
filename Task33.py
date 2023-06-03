# Задача 33: Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные.
# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот:
# все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]
# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]
def replace_max_by_min(list_n):
    temp_list = list_n.copy()    # Создали temp_list, чтобы избежать side effects функции
    max_grades = max(temp_list)
    min_grades = min(temp_list)
    for i in range(len(temp_list)):
        if temp_list[i] == max_grades:
            temp_list[i] = min_grades
    return temp_list
# print(list_1)
print(replace_max_by_min(list_1))
# print(list_1)

# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None

# list_1 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
# def replace_max_by_min(list_n):
#     temp_list = list_n.copy()
#     max_grades = max(temp_list)
#     min_grades = min(temp_list)
#     if min_grades == max_grades:
#             return None
#     for i in range(len(temp_list)):
#         if temp_list[i] == max_grades:
#             temp_list[i] = min_grades
#     return temp_list
# print(replace_max_by_min(list_1))

# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.

# list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# def replace_max_by_min(list_n, who):
#     temp_list = list_n.copy()
#     max_grades = max(temp_list)
#     min_grades = min(temp_list)
#     for i in range(len(temp_list)):
#         if who == "enemy":
#             if temp_list[i] == max_grades:
#                 temp_list[i] = min_grades
#         if who == "friend":
#             if temp_list[i] == min_grades:
#                 temp_list[i] = max_grades
#     return temp_list
# print(replace_max_by_min(list_1, "enemy"))
# print(replace_max_by_min(list_1, "friend"))