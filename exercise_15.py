import json

with open('csv_file.csv', 'r') as f:
    data = [x.strip().split(',') for x in f.readlines()]

json_content = []
for line in data:
    d = {'club': line[0], 'city': line[1], 'country': line[2]}
    json_content.append(d)

json_f = open('json_file.txt', 'w+')
json.dump(json_content,json_f)
json_f.close()