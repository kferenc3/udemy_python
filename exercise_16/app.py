from addition import Addition

class Calculator(Addition):
    @classmethod
    def add(cls,num1,num2):
        return Addition.add(num1,num2)
    
    @classmethod
    def multiply(cls, num1, num2):
        n = 0
        for _ in range(num2):
            n = Addition.add(n, num1)
        return n
    
    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)
    
    @classmethod
    def divide(cls, num1, num2):
        n = 0
        while num1 >= num2:
            num1 = cls.subtract(num1,num2)
            n = cls.add(n, 1)
        return n

print(Calculator.multiply(6,3))
print(Calculator.divide(8,2))            