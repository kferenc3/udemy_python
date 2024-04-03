class Salary:
    def calculate(self, hours):
        return self.rate * hours

class Promotable:
    def promote(self, value: int):
        self.rate += value

class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate    # hourly salary
 
    def weekly_salary(self) -> float:
        return self.calculate(40)   