# Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования
# в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from collections import Counter

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
counter = Counter(my_list)

new_list = [el for el, n in counter.items() if n == 1]
print(new_list)