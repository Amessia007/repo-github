# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

array = list(input('enter a sequence of numbers: '))
i = 0
if len(array) % 2 == 0:
    while i < len(array):
        num = array[i]
        array[i] = array[i + 1]
        array[i + 1] = num
        i = i + 2
else:
    while i < len(array) - 1:
        num = array[i]
        array[i] = array[i + 1]
        array[i + 1] = num
        i = i + 2
print(array)
