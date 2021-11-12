# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict


month = int(input('enter the month number:'))

season = ['spring', 'summer', 'autumn', 'winter', 'not a month']


month_dict = {1: 'January', 2: 'February',
              3: 'March', 4: 'April', 5: 'May',
              6: 'June', 7: 'Jule', 8: 'August',
              9: 'September', 10: 'October', 11: 'November',
              12: 'December'}
month_list = list(month_dict.values())
if 1 <= month <= 12:
    for i, el in enumerate(month_list):
        if i == month - 1:
            print(f"Month from list is {month_list[i]}")
            break
    print(f"Month from dict is {month_dict[month]}")

    if 3 <= month <= 5:
        season_index = int(0)
    elif 6 <= month <= 8:
        season_index = int(1)
    elif 9 <= month <= 11:
        season_index = int(2)
    elif 1 <= month <= 2 or month == 12:
        season_index = int(3)
    elif 0 <= month >= 13:
        season_index = int(4)
    print(f'{month_dict[month]} is {season[season_index]}')
else: print("You made a mistake")


