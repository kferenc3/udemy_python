import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file)
file.close()

print(file_contents['friends'][0]['name'])