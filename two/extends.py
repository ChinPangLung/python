class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')
class Cat(Animal):
    def run(self):
        print('Cat is running')
    def eat(self):
        print('cat is eatting')
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

dog=Dog()
dog.run()
cat=Cat()
cat.run()
cat.eat()

#静态语言和动态语言
class Timer(object):
    def run(self):
        print('start....')

# 多态
def run_twice(animal):
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

run_twice(Timer())

