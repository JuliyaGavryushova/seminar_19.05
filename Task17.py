# Задача 17: Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# Примеры/Тесты:
# [1, 1, 2, 0, -1, 3, 4, 4] -> 6
# [1, 1, 2, 0, 1, 2, 1, 2] -> 3

list_1 = [1, 1, 2, 0, 1, 2, 1, 2]
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)
print(len(list_2))