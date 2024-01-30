import re
 
def is_filename_safe(filename):
    regex = '^[a-zA-Z0-9]+[a-zA-Z0-9-_()]*\.(jpg|jpeg|png|gif)$'
    return re.match(regex, filename) is not None

print(is_filename_safe('Afsgfs_esge(asdaf).jpeg'))