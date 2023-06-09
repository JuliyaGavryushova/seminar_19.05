# Задача 25: Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Примеры/Тесты:
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Input: a b c d a a a a a a a
# Output: a b c d a_1 a_2 a_3 a_4 a_5 a_6 a_7
# Строку не обязательно вводить с клавиатуры

s = "a a a b c a a d c d d"
amount_of_letters = dict()
output_string = ""
for el in s:
    if el != " ":
        if el not in amount_of_letters:
            amount_of_letters[el] = 1
            output_string += el
        else:
            output_string += el + "_" + str(amount_of_letters[el])
            amount_of_letters[el] += 1
    else:
        output_string = output_string + el
print(output_string)