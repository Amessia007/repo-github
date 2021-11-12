# * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные
# у пользователя.
# Необходимо собрать аналитику о товарах. Р
# еализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.

product_number = []
counter = 0
goods = []
while input("Would you like to add product? Enter y/n ") == 'y':
    product_number.insert(counter, counter + 1)
    counter = counter + 1
    print(f'product_number {product_number}')
    name = input('input name: ')
    price = input('price: ')
    quantity = input('quantity: ')
    unit_of_measure = input('unit_of_measure: ')
    product = counter, {'name': name, 'price': price, 'quantity': quantity, 'unit of measure': unit_of_measure}
    goods.insert(counter, product)
    print(goods, type(goods))

else:
    goods_save = tuple(goods)
    print(type(goods_save))


goods_analis = dict(goods)
print(type(goods_analis))
print(goods_analis)
print(goods_analis.keys())
print(goods_analis.values())
print(goods_analis.get('name'))
print(goods_analis.get('price'))
print(goods_analis.get('quantity'))
print(goods_analis.get('unit of measure'))
print(goods_analis.items())
