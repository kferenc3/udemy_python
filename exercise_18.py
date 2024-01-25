class PrimeGenerator:
    def __init__(self, bound) -> None:
        self.bound = bound
        self.start = 2

    def __next__(self):
        for n in range(self.start,self.bound):
            for x in range(2, int(n/2)+1):
                if n % x == 0:
                    break
            else:
                self.start = n + 1
                return n
        raise StopIteration

pg = PrimeGenerator(1000)

class FirstHundredGenerator:
    def __init__(self) -> None:
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration
    
    def __iter__(self):
        return self

# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator()
    
print(sum(FirstHundredGenerator()))
