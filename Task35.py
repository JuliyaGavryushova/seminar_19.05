# Задача 35: Напишите функцию, которая принимает число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число
# Если число простое - функция возвращает True, если нет - возвращает False
# Примеры/Тесты:
# <function_name>(13) -> True
# <function_name>(10) -> False

# def prime_number(n):
#     if isinstance(n, int):
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
# print(prime_number(10))

# def prime_number(n):
#     if not isinstance(n, int):
#         return "Error"
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(prime_number(10))

def prime_number(n: int) -> bool:        # Тайп хинтинг (type hints)/ Аннотация типов
    if not isinstance(n, int):
        return "Error"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(prime_number(10))