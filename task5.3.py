# -*- coding: utf-8 -*-
'''Создать текстовый файл (не программно), построчно
записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

with open('text5.3.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Salary less than 20,000 rub: {poor})')
print(f'Average salary {sum(map(int, sal)) / len(sal)} rub')

