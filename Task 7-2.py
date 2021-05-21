# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
# костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return self.calc + other.calc

class Coat(Clothes):

    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print("Минимальный размер 40")
            self.__size = 40
        elif size > 60:
            print("Максимальный размер 60")
            self.__size = 60
        else:
            self.__size = size

    @property
    def calc(self):
        return self.__size / 6.5 + 0.5

class Suit(Clothes):

    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 90:
            print("Минимальный рост 90")
            self.__height = 90
        elif height > 240:
            print("Максимальный размер 240")
            self.__height = 240
        else:
            self.__height = height

    @property
    def calc(self):
        return (2 * self.__height + 0.3) / 100


coat_1 = Coat(int(input("Введите размер для пальто: ")))
print(f"Расход ткани на пальто {coat_1.size} размера {coat_1.calc:.2f} метров")
suit_1 = Suit(int(input("Введите рост для костюма: ")))
print(f"Расход ткани на костюм {suit_1.height} роста {suit_1.calc:.2f} метров")
print(f"Общий расхода ткани: {coat_1 + suit_1:.2f} метров")
