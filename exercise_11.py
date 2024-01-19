def count_from_zero_to_n(n):
    if n<0:
        raise ValueError('Only positive integers are accepted')
    for x in range(0, n+1):
        print(x)