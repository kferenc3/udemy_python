def prime_generator(bound):
    for n in range(2,bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n

g = prime_generator(1000)
print(next(g))