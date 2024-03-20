import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')

def complex_calculation():
    start = time.time()
    print('started calculating...')
    [x**2 for x in range(200000000)]
    print(f'complex_calculation, {time.time() - start}')

start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

# thread1 = Thread(target=complex_calculation)
# thread2 = Thread(target=ask_user)

start = time.time()
# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

#pool.shutdown() --> if not using context manager


print(f'Two thread total time: {time.time() - start}')