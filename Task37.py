# Задача 37: Напишите функцию, которая принимает натуральное число n,
# в теле функции считывает (input) последовательность из n элементов
# Возвращает эту последовательность в виде строки в обратном порядке
# Примеры/Тесты:
# <function_name>(5) 1 2 3 4 5 -> '5 4 3 2 1'
# <function_name>(3) 8 7 9 -> '9 7 8'
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

def string_reverse(n):
    string_num = input()
    if n == 1:
        return string_num
    return string_reverse(n - 1) + " " + string_num
print(string_reverse(5))