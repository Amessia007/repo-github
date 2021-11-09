'''Реализовать класс Road (дорога), в котором определить
атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''

class Road:

    def __init__(self, length, width, weight, height):
        self._length = length
        self._width = width
        self.weight = weight
        self.height = height

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print('Mass', int(asphalt_mass), 'tons')


r = Road(5000, 20, 25, 5)
r.asphalt_mass()
