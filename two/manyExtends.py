class Animal(object):
    pass


class Runnable(object):
    def run(self):
        print('Running....')


class Flyable(object):
    def fly(self):
        print('fly....')


class Mammal(Animal):
    pass


class Brid(Animal):
    pass


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parot(Brid):
    pass


class Ostrich(Brid):
    pass
