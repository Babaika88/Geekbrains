import random


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = True

    def show_speed(self):
        print(f"{self.name} едет со скоростью {self.speed}")


class TownCar(Car):
    def go(self):
        print(f"Машина {self.name} Go - Go")

    def stop(self):
        print(f"Машина {self.name} Stop")

    def turn(self):
        i = random.random()
        if i > 0.5:
            print(f"Машина {self.color} поехала направо")
        else:
            print(f"Машина {self.color} поехала налево")

    def show_speed(self):

        if self.speed > 60:
            print(f"Машина {self.name} превышает  скорость")
        else:
            print("Скорость норм")


class SportCar(Car):
    def go(self):
        print(f"Машина {self.name} Go - Go")

    def stop(self):
        print(f"Машина {self.name} Stop")

    def turn(self):
        i = random.random()
        if i > 0.5:
            print(f"Машина {self.color} поехала направо")
        else:
            print(f"Машина {self.color} поехала налево")


class WorkCar(Car):
    def go(self):
        print(f"Машина {self.name} Go - Go")

    def stop(self):
        print(f"Машина {self.name} Stop")

    def turn(self):
        i = random.random()
        if i > 0.5:
            print(f"Машина {self.color} поехала направо")
        else:
            print(f"Машина {self.color} поехала налево")

    def show_speed(self):
        if self.speed > 40:
            print("Машина превышает скорость")
        else:
            print("Скорость норм")


class PolisCar(Car):
    def go(self):
        print(f"Машина {self.name} Go - Go")

    def stop(self):
        print(f"Машина {self.name} Stop")

    def turn(self):
        i = random.random()
        if i > 0.5:
            print(f"Машина {self.color} поехала направо")
        else:
            print(f"Машина {self.color} поехала налево")


t = TownCar(70, "blue", "kia")
t.go()
t.stop()
t.show_speed()
t.turn()
print()
s = SportCar(120, "black", "hyndai")
s.go()
s.stop()
s.show_speed()
s.turn()
print()
w = WorkCar(40, "yellow", "Белорус")
w.go()
w.stop()
w.show_speed()
w.turn()
print()
p = PolisCar(1000, "blue-white", "Reno")
p.go()
p.stop()
p.show_speed()
p.turn()
