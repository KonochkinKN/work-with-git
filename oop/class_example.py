import random


class Car:
    __color = (0, 0, 255)
    __year = 2000
    __condition = {'tires': 100,
                   'engine': 100,
                   'fuel': 100,
                   'glass': 100,
                   'body': 100}

    def __init__(self, brand, model):
        """ инициализация """
        self.brand = brand
        self.model = model

    def change_year(self, year):
        if 1970 <= year <= 2024:
            self.__year = year

    def change_color(self, new_color):
        """ перекрасить """
        if all([0 <= c <= 255 for c in new_color]):
            self.__color = new_color

    def change_condition(self, part, value):
        if value > 100 or value < 0:
            print('invalid value:', value)
            return
        if part in self.__condition.keys():
            self.__condition[part] = value
        else:
            print('invalid part:', part)

    def show_condition(self):
        print('Condition:')
        for part in self.__condition.keys():
            print(f'{part}:\t{self.__condition[part]}')

    def crash(self, level):
        print(f'crash level: {level}')
        if level == 'low':
            self.__condition['body'] -= random.randint(5, 20)
            self.__condition['glass'] -= random.randint(0, 10)
        elif level == 'medium':
            self.__condition['body'] -= random.randint(10, 40)
            self.__condition['glass'] -= random.randint(5, 30)
            self.__condition['engine'] -= random.randint(0, 10)
        elif level == 'high':
            self.__condition['body'] -= random.randint(30, 80)
            self.__condition['glass'] -= random.randint(30, 80)
            self.__condition['engine'] -= random.randint(10, 50)
        elif level == 'total':
            self.__condition['body'] -= random.randint(50, 95)
            self.__condition['glass'] -= random.randint(50, 95)
            self.__condition['engine'] -= random.randint(30, 70)

    def __str__(self):
        return f'{self.brand} {self.model},' \
               f' color: {self.__color}, year: {self.__year}'


class Kia(Car):
    def __init__(self, model, year=2000, color=(0, 255, 0)):
        super().__init__('Kia', model, year, color)


class KiaRio(Kia):
    def __init__(self, year=2000, color=(0, 255, 0)):
        super().__init__('Rio', year, color)


def test():
    # ford = Car(brand='Ford', model='Focus', year=2005)
    # print(ford)
    # ford.change_color((255, 0, 0))
    # print(ford)
    # ford.show_condition()
    # ford.crash(random.choice(['low', 'medium', 'high', 'total']))
    # ford.show_condition()
    kia = Kia(model='Picanto', year=2010)
    print(kia)
    kia.show_condition()
    kia_rio = KiaRio()
    print(kia_rio)

    print(issubclass(KiaRio, Kia))
    print(issubclass(KiaRio, Car))

    print(isinstance(kia_rio, KiaRio))
    print(isinstance(kia_rio, Kia))
    print(isinstance(kia_rio, Car))


if __name__ == '__main__':
    ford = Car(brand='Ford', model='Focus')
    ford.change_color((0, 0, 0))
    print(ford)
    ford.change_condition('engine', 80)
    ford.show_condition()
