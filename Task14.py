# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8

# n = int(input("Введите число N: "))
# exp = 0
# i = 0
# while exp <= n:
#     exp = 2 ** i
#     if exp <= n:
#         print(exp)
#         i += 1

#  (*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. 
# Для этого воспользоваться параметрами функции print
# Примеры/Тесты:
# 10     -> 1,2,4,8,
# 10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,

n = int(input("Введите число N: "))
exp = 0
i = 0
print(n, end = " -> ")
while exp <= n:
    exp = 2 ** i
    if exp <= n:
        i += 1
        print(exp, end = ", ")