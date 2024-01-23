from utils import database

def menu(myshelf):
    USER_CHOICE="""------------------------
AwesomeBookDatabase3001
------------------------
Please select an option:
- Type 'a' for adding a new book,
- Type 'l' for listing all books,
- Type 'r' to mark a book as read,
- Type 'd' to delete a book from the database,
- Type 'o' to load books from a file,
- Type 'w' to write the current list to a file,
- Type 'q' to quit
Your choice: """

    opt = input(USER_CHOICE).lower()
    while opt != 'q':
        if opt == 'a':
            inp_string = input('Please add the name and author of the book separated by commas: ').strip()
            read_str = input('Did you read this book? y/n')
            try:
                myshelf.add_book(inp_string, read_str)
            except ValueError:
                print('The input format is not valid. Book not added.')
        elif opt == 'l':
            myshelf.list_books()
        elif opt == 'o':
            overwrite = input('WARNING! This will overwrite your current books. Are you sure you want to continue? y/n ')
            if overwrite =='y':
                myshelf.load_from_file('/Users/ferenc.kiss/udemy_python/milestone_2/filestore.txt')
        elif opt == 'r':
            search_string = input('Please enter the name of the book you wish to mark as read: ')
            result = myshelf.mark_read(search_string)
            if result:
                print('Success!')
            else:
                print("The requested book is not found.")
            pass
        elif opt == 'd':
            search_string = input('Please enter the book name you wish to delete: ')
            myshelf.delete_book(search_string)
        elif opt == 'w':
            myshelf.write_to_file('filestore.txt')
        elif opt not in ['a','l','o','r','d','w','q']:
            print('\nINVALID OPTION!')
        opt = input(USER_CHOICE).lower()
    print('Bye!')

if __name__ == '__main__':
    myshelf = database.Bookshelf()
    menu(myshelf)