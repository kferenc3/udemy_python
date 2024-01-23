import json

class Bookshelf:
    def __init__(self):
        self.shelf = []

    def add_book(self, input_str, r):
        try:
            name, author = input_str.split(',')
        except ValueError:
            raise
        if r == 'y':
            self.shelf.append({'name': name, 'author': author, 'read': True})
        else:
            self.shelf.append({'name': name, 'author': author, 'read': False})

    def mark_read(self, search):
        for book in self.shelf:
            if book['name'] == search:
                book['read'] = True
                return True
        return False
    
    def list_books(self):
        cnt = 1
        for book in self.shelf:
            print(f'Book {cnt}')
            print(f'Name: {book["name"]}\nAuthor: {book["author"]}\nRead: {book["read"]}')
            cnt += 1
    
    def delete_book(self, search):
        self.shelf = [book for book in self.shelf if book['name']!=search]

    def load_from_file(self, fname):
        with open(fname, 'r') as f:
            self.shelf = json.load(f)
    
    def write_to_file(self, fname):
        with open(fname, 'w+') as f:
            json.dump(self.shelf, f)


if __name__ == '__main__':
    myshelf = Bookshelf()
    myshelf.add_book('Lotr', 'Tolkien')
    myshelf.list_books()
    myshelf.load_from_file('/Users/ferenc.kiss/udemy_python/milestone_2/filestore.txt')
    myshelf.list_books()
    