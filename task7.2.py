'''Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. '''

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        pass

    @abstractmethod
    def abstract(self):
        return 'Smth very abstract'


class Coat(Clothes):
    def consumption(self):
        return f'For sewing a coat you need: {self.param / 6.5 + 0.5 :.2f}m of fabrics'

    def abstract(self):
        return f'{self.param / 6.5 + 0.5 :.2f}'


class Suit(Clothes):
    def consumption(self):
        return f'To sew a suit you need: {2 * self.param + 0.3 :.2f}m of fabrics'

    def abstract(self):
        return f'{2 * self.param + 0.3 :.2f}'


coat = Coat(50)
suit = Suit(187)

print(coat.consumption())
print(suit.consumption())
print(f'You need {float(coat.abstract()) + float(suit.abstract())}m of fabrics for all.')
print(Clothes.abstract('self'))



