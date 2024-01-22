#from ..find import NotFoundError  --> relative import from parent

def save_to_file(content, filename):
    with open(filename, 'w+') as f:
        f.write(content)


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()