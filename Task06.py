# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

# number = int(input("Введите шестизначный номер билета: "))
# if number > 99999 and number < 1000000:
#     digit1 = number // 100000
#     digit2 = number // 10000 % 10
#     digit3 = number // 1000 % 10
#     digit4 = number // 100 % 10
#     digit5 = number // 10 % 10
#     digit6 = number % 10
#     part1 = digit1 + digit2 + digit3
#     part2 = digit4 + digit5 + digit6
#     if part1 == part2:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("Вы ввели некорректный номер билета!")

# (*) Усложнение. Вывод результата сделайте одной строкой, для этого используйте тернарный оператор:

number = int(input("Введите шестизначный номер билета: "))
if number > 99999 and number < 1000000:
    digit1 = number // 100000
    digit2 = number // 10000 % 10
    digit3 = number // 1000 % 10
    digit4 = number // 100 % 10
    digit5 = number // 10 % 10
    digit6 = number % 10
    part1 = digit1 + digit2 + digit3
    part2 = digit4 + digit5 + digit6
    print("yes" if part1 == part2 else "no")
else:
    print("Вы ввели некорректный номер билета!")