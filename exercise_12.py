class UncountableError(ValueError):
    def __init__(self, wrong_value) -> None:
        super().__init__(f'Invalid value for n, {wrong_value}. n must be greater than 0.')

def count_from_zero_to_n(n):
    if n<0:
        raise UncountableError(n)
    for x in range(0, n+1):
        print(x)


count_from_zero_to_n(-10)