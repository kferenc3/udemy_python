from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    dd = defaultdict(lambda: 'Unknown')
    dd['Alan'] = 'Manchaster'
    return dd

def task2(arg_od: OrderedDict):

    arg_od.popitem(True)
    arg_od.popitem(False)
    arg_od.move_to_end('Bob',last=True)
    arg_od.move_to_end('Dan',last=False)

def task3(name: str, club: str) -> namedtuple:
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name, club)
    return player

def task4(arg_deque: deque):
    arg_deque.pop()
    arg_deque.rotate(-1) #equivalent to arg_deque.append(arg_deque.popleft())
    arg_deque.appendleft('Zack')