class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)

    def __getitem__(self,i):
        return self.players[i]
    
    def __len__(self):
        return len(self.players)
    
    def __repr__(self):
        return f'<Club {self.name}: {self.players}>'
    
    def __str__(self):
        return f'The Club {self.name} has the following {len(self)} players: ' +', '.join(self.players)
    
myclub = Club('Makkoshotyka FC')
myclub.add_player('Jozsi')
myclub.add_player('Gazsi')

print(myclub)

"""
inheritence:

class A:
    def __init__(self, a ,b):
        self.a = a
        self.b = b

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

@property decorator --> treating a function method as a property. e.g def average() --> no action function, only returns a value
"""