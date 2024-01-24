from .database_connect import DatabaseConnection

# def create_book_table(conn):
#     cursor = conn.cursor()
#     cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
#     conn.commit()
class Bookshelf:
    def __init__(self):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    def add_book(self, name, author, r):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO books VALUES(?, ?, ?)', (name, author, True if r=='y' else False))

    def mark_read(self, search):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT read FROM books WHERE name = ?', (search,))
            r = 1 if cursor.fetchall()[0][0] == 0 else 0
            cursor.execute('UPDATE books SET read = ? WHERE name = ?', (r, search))
            rc = cursor.rowcount
        return rc
    
    def get_all_books(self):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM books')
            books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        return books

    def delete_book(self, search):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM BOOKS where name = ?', (search,))
            rc = cursor.rowcount
        return rc