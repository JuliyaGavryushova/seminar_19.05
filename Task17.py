# Задача 17: Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# Примеры/Тесты:
# [1, 1, 2, 0, -1, 3, 4, 4] -> 6
# [1, 1, 2, 0, 1, 2, 1, 2] -> 3

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list_2 = []
# for i in list_1:
#     if i not in list_2:
#         list_2.append(i)
# print(list_2)
# print(len(list_2))

# Решение через множество:

print(len(set(list_1)))

# Бонусная задача 1: Дан список, содержащий искаженные данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду?
# Можно ли при этом не создавать новый список?

# lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# for el in lst:
#     el = el.split()
#     rez_str = "Привет, " + el[-1].title() + "!"
#     print(rez_str)