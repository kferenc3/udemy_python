class Car:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def __repr__(self) -> str:
        return f'<Car {self.make} {self.model}'

class Garage:
    def __init__(self) -> None:
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def add_cars(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)


ford = Garage()
#ford.add_cars('fiesta')
car = Car('Ford', 'Fiesta')

try:
    ford.add_cars(car)
except TypeError:
    print("Your car was not a car.")

print(len(ford))