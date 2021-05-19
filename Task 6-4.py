# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {'направо' if direction == 1 else 'налево'}")

    def show_speed(self):
        print(f"{self.name} едет со скоростью {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} едет со скоростью {self.speed}! Это превышение!")
        else:
            print(f"{self.name} едет со скоростью {self.speed}.")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} едет со скоростью {self.speed}! Это превышение!")
        else:
            print(f"{self.name} едет со скоростью {self.speed}.")

class SportCar(Car):
    def show_speed(self):
        if self.speed < 160:
            print(f"{self.name} едет со скоростью {self.speed}! Это не предел!")
        else:
            print(f"{self.name} едет со скоростью {self.speed}.")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

town_car = TownCar(65, "красная", "Toyota RAV4")
town_car.go()
town_car.show_speed()
town_car.turn(1)

work_car = WorkCar(55, "желтый", "MAN")
work_car.go()
work_car.show_speed()
work_car.stop()

sport_car = SportCar(150, "оранжевый", "Ferrari")
sport_car.go()
sport_car.show_speed()
sport_car.turn(0)

police_car = SportCar(100, "белая", "Audi RS6")
police_car.go()
police_car.show_speed()
police_car.turn(0)