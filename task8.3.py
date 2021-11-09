'''Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.'''


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
inp_data = input("Введите stop чтобы прервать цикл. \nВведите y чтобы продолжить: ")

while str(inp_data) != 'stop':
    inp_data = input("Введите положительное число: ")
    try:
        inp_data = int(inp_data)
        if inp_data < 0:
            raise OwnError("Вы ввели отрицательное число!")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        num_list.append(inp_data)
        print("Список чисел", inp_data, num_list)
else:
    print("Окончательный список чисел", num_list)

