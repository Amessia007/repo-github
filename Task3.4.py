# Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения
# числа в степень.


def my_func(x, y):
    return x ** y
print(my_func(3, -3))

def my_func2(x, y):
    if y < 0:
        c = int(0)
        answer = 1
        while c >= y:
            print(c)
            c = int(c - 1)
            answer = answer / x
        else:
            while c <= y:
                c = c + 1
                answer = answer * x
            return answer


print(my_func(3, -3))