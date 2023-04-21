# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 ->

def exponentiation_rec(base, exponent):
    if exponent == 0:
        return 1
    result = base * exponentiation_rec(base, exponent - 1)
    return result


a = int(input('Введите основание степени: '))
b = int(input('Введите показатель степени: '))
print(f'{a} в степени {b} равно {exponentiation_rec(a, b)}')
