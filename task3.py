'''
Створіть клас автомобіля з такими атрибутами: марка, модель, рік випуску та швидкість.
Клас Car повинен мати такі способи: розгін, гальмування та display_speed.
Метод прискорення повинен збільшити швидкість на 5, а гальмівний - на 5.
Пам'ятайте, що швидкість не може бути негативною.
'''
class Car:
    def __init__(self, brand, model, year, speed=250):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    def up_speed(self):
        self.speed += 5
    def down_speed(self):
        if self.speed -5 >= 0:
            self.speed -=5
        else:
            self.speed = 0
    def speed_on_display(self):
        print(f'Швидкість авто: {self.speed}')

Lamborghini = Car('Lamborghini', 'Aventador', 2022)
Lamborghini.up_speed()
Lamborghini.speed_on_display()
Lamborghini.down_speed()
Lamborghini.speed_on_display()