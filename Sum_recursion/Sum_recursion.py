# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Пример:
# 2 2
# 4
def Sum_rec(number1, number2):
    if number2 == 0:
        return number1
    result = Sum_rec(number1, number2 - 1) + 1
    return result


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(f'Сумма этих чисел равна {Sum_rec(a, b)}')
