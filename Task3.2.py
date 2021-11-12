# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def person():
    name = input('name: ')
    surname = input('surname: ')
    year_of_birth = input('year of birth: ')
    city_of_residence = input('city of residence: ')
    email = input('email: ')
    telephone = input('telephone: ')
    return name + surname + year_of_birth + city_of_residence + email + telephone

print(person())