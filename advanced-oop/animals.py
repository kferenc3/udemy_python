from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print("Walking...")

    @abstractmethod
    def num_legs(self):
        pass



class Dog(Animal):
    def __init__(self, name) -> None:
        self.name = name
    
    def num_legs(self):
        return 4
    

class Monkey:
    def __init__(self, name) -> None:
        self.name = name

    def num_legs(self):
        return 2