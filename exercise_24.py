from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def hungry(self):
        print('I want to eat {}!'.format(self.get_favourite_food()))
    
    @abstractmethod
    def get_favourite_food(self):
        pass
 
 
class Dog(Animal):
    def __init__(self, name):
        self.name = name
 
    @classmethod
    def get_favourite_food(cls):
        return 'ribs'