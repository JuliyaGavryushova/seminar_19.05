# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом.
# На входе задано количество ягод на каждом кусте. 
# Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы
# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7
# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = []
for i in range(0, len(list_1)):
    if i == 0:
        list_2.append(list_1[i] + list_1[i + 1] + list_1[len(list_1) - 1])
    elif i == len(list_1) - 1:
        list_2.append(list_1[i] + list_1[i - 1] + list_1[0])
    else:
        list_2.append(list_1[i - 1] + list_1[i] + list_1[i + 1])
max_element = list_2[0]
max_index = 0
for i in range(0, len(list_2)):
    if list_2[i] > max_element:
        max_element = list_2[i]
        max_index = i
print(f"Макс. кол-во ягод {max_element}, собрано для куста {max_index + 1}")