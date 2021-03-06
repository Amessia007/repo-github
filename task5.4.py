# -*- coding: utf-8 -*-
'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text5.4.txt', 'r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])

print(f'{new_file}')

with open('text5.4_ver2.txt', 'w') as my_file_ver2:
    my_file_ver2.writelines(new_file)
