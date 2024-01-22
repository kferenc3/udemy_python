while True:
    friends_set= set([x.strip().lower() for x in input('Enter the name of 3 friends, separated by a comma: ').split(',')])
    if len(friends_set) == 3:
        break
    else:
        print('The friend list should be exactly 3 people long. Please try again!')

with open('people.txt','r') as f:
    people = set([x.replace('\n','').lower() for x in f.readlines()])

nf = open('nearby_friends.txt', 'a')
nearby = friends_set.intersection(people)

for friend in nearby:
    print(f'{friend.title()} is nearby!')
    nf.write(friend.title()+'\n')

nf.close()