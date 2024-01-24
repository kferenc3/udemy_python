from utils import database

def menu(myshelf):
    USER_CHOICE="""------------------------
AwesomeBookDatabase3001
------------------------
Please select an option:
- Type 'a' for adding a new book,
- Type 'l' for listing all books,
- Type 'r' to mark a book as read/unread,
- Type 'd' to delete a book from the database,
- Type 'q' to quit
Your choice: """

    opt = input(USER_CHOICE).lower()
    while opt != 'q':
        if opt == 'a':
            prompt_add_book()
        elif opt == 'l':
            list_books()
        elif opt == 'r':
            prompt_mark_read()
        elif opt == 'd':
            prompt_delete()
        elif opt not in ['a','l','r','d','q']:
            print('\nINVALID OPTION!')
        opt = input(USER_CHOICE).lower()
    print('Bye!')

def prompt_add_book():
    name = input('Please enter the name of the book: ').strip()
    author = input('Please enter the author of the book: ').strip()
    read_str = input('Did you read this book? (y/n) ')
    myshelf.add_book(name, author, read_str)

def list_books():
    books = myshelf.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_mark_read():
    search_string = input('Please enter the name of the book you wish to mark as read/unread: ')
    updated = myshelf.mark_read(search_string)
    if updated > 0:
        print('Success!')
    else:
        print('The requested book could not be found.')

def prompt_delete():
    search_string = input('Please enter the book name you wish to delete: ')
    deleted = myshelf.delete_book(search_string)
    if deleted > 0:
        print('Success!')
    else:
        print('The requested book could not be found.')

if __name__ == '__main__':
    myshelf = database.Bookshelf()
    menu(myshelf)