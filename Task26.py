# Задача 26: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def exponentiation(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return exponentiation(x, n // 2) * exponentiation(x, n // 2)
    return exponentiation(x, n - 1) * x

print(exponentiation(2, 4))
