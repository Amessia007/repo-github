# -*- coding: utf-8 -*-
'''Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.'''

with open('text5.5.txt', 'w+') as my_file:
    my_list = [el for el in range(20, 200)]
    print(f'{my_list}', file=my_file)

print(sum(map(int, my_list)))