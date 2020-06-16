from random import randrange


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
# базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите
# результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехал")

    def stop(self):
        print(f"{self.name} остановился")

    def turn(self, direction=None):
        direct_list = ["назад", "прямо", "налево", "направо"]
        a_direction = direction
        if a_direction == None:
            a_direction = direct_list[randrange(0, 3)]
        else:
            a_direction = direct_list[a_direction]
        print(f"{self.name} движется {a_direction}")

    def show_speed(self):
        print(f"Скорость {self.name} = {self.speed} км/час")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        limit = 60
        if self.speed > limit:
            print(f"Для {self.name} превышена скорость = {limit} км/час")
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        limit = 40
        if self.speed > limit:
            print(f"Для {self.name} превышена скорость = {limit} км/час")
        else:
            super().show_speed()


Base = Car(60, 'зеленый', 'Телега', False)
print(Base.name, Base.color, Base.speed, Base.is_police, sep=", ")
Base.go()
Base.turn(1)
Base.show_speed()
Base.stop()
print()
mySport = Car(120, 'красный', 'Lamborghini', False)
print(mySport.name, mySport.color, mySport.speed, mySport.is_police, sep=", ")
mySport.go()
mySport.turn()
mySport.turn()
mySport.show_speed()
mySport.stop()
print()
aPolice = PoliceCar(90, 'голубой', 'Wolkswagen', True)
print(aPolice.name, aPolice.color, aPolice.speed, aPolice.is_police, sep=", ")
aPolice.go()
aPolice.show_speed()
aPolice.turn(1)
aPolice.turn(2)
aPolice.stop()
print()
aTownCar = TownCar(65, 'желтый', 'Fiat', False)
print(aTownCar.name, aTownCar.color, aTownCar.speed, aTownCar.is_police, sep=", ")
aTownCar.go()
aTownCar.show_speed()
aTownCar.stop()
print()
aWorkCar = WorkCar(30, 'серый', 'HOWO', False)
print(aWorkCar.name, aWorkCar.color, aWorkCar.speed, aWorkCar.is_police, sep=", ")
aWorkCar.go()
aWorkCar.show_speed()
aWorkCar.turn(3)
aWorkCar.turn()
aWorkCar.stop()
