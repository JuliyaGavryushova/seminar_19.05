# Задача 7.1: Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: 
# [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. 
# Сформировать путь к нему с использованием
# os.path и pathlib

# import os
# import os.path as path1
# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# file_name = path1.join(MAIN_DIR, "Data1.txt")

# with open (file_name, mode="r", encoding="utf-8") as data:
#     result_list = []
#     for item in data:
#         last_name, first_name, second_name = item.strip().split("#")
#         print(last_name, first_name, second_name)
#         list_1 = [last_name, first_name, second_name]
#         result_list.append(list_1)
#     print(result_list)

# Задача 7.2: Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И
# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много.
# Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым?

# import os
# import os.path as path1
# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# file_name = path1.join(MAIN_DIR, "Data1.txt")

# with open (file_name, mode="r", encoding="utf-8") as data:
#     result_list = []
#     for item in data:
#         last_name, first_name, second_name = item.strip().split("#")
#         list_1 = [last_name, first_name, second_name]
#         result_list.append(list_1)

# for item in result_list:
#     str_1 = item[0] + " " + item[1][0] + "." + item[2][0] + "."
#     print(str_1)

# for last_name, first_name, second_name in result_list:
#     str_1 = f"{last_name} {first_name[0]}.{second_name[0]}"
#     print(str_1)

# [*] Усложнение. Данные необходимо записать в два разных файла:

import os
import os.path as path1
MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR, "Data1.txt")

with open (file_name, mode="r", encoding="utf-8") as data:
    result_list = []
    for item in data:
        last_name, first_name, second_name = item.strip().split("#")
        list_1 = [last_name, first_name, second_name]
        result_list.append(list_1)

file_name_2 = path1.join(MAIN_DIR, "Results", "Names.txt")

with open (file_name_2, mode="wt", encoding="utf-8") as result_file:
    for last_name, first_name, second_name in result_list:
        str_1 = f"{last_name} {first_name[0]}.{second_name[0]}.\n"
        result_file.write(str_1)

