# Задача 35: Напишите функцию, которая принимает число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число
# Если число простое - функция возвращает True, если нет - возвращает False
# Примеры/Тесты:
# <function_name>(13) -> True
# <function_name>(10) -> False

num = int(input("Введите число: "))
def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
print(prime_number(num))