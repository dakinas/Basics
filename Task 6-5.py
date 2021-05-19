# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title="кисточкой", color="черной", figure="круг"):
        self.title = title
        self.color = color
        self.figure = figure

    def draw (self):
        print(f"Начинаем рисовать {self.color} {self.title} ")

class Pen(Stationery):
    def draw(self):
        print(f"Начинаем рисовать {self.color} ручкой {self.title} {self.figure}")

class Pencil(Stationery):
    def draw(self):
        print(f"Начинаем рисовать {self.color} карандашем {self.title} {self.figure}")

class Handle(Stationery):
    def draw(self):
        print(f"Начинаем рисовать {self.color} маркером {self.title} {self.figure}")

stat = Stationery()
stat.draw()
pen = Pen("Parker", "синей", "линию")
pen.draw()
pencil = Pencil("Big", "красным", "квадрат")
pencil.draw()
handle = Handle("Erich Krause", "желтым", "овал")
handle.draw()