from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

def greet(g):
    #yield from g -> alternative
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

# def greet():
#     friend = yield
#     print(f'Hello, {friend}')


# g  = greet()
# g.send(None) # priming the generator. essentially bringing the function up to the first yield
# g.send('Adam')