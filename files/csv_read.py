f = open('csv_data.csv', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

lines = lines[1:]

for line in lines:
    dat = line.split(',')
    name = dat[0].title()
    age = dat[1]
    uni = dat[2].title()
    deg = dat[3].capitalize()

    print(f'{name} is {age} years old and studying {deg} at {uni}')

"""
import csv

writer = csv.DictWriter(f, fieldnames=a, b)
writer.writeheader()
writer.writerows(dictionary)

reader = csv.DictReader(f)
"""