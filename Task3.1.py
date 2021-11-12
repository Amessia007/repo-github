# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.


def division():
    try:
        dividend = float(input('dividend: '))
        divider = float(input('divider: '))
        div = dividend / divider
    except ZeroDivisionError:
        print('you cannot divide by zero')
        return
    return div

print(division())