class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow! Bow!")

bull_dog = Dog()
bull_dog.bark()