user = {
    'id': 1,
    'name': 'Jose',
    'role': 'admin'
}

def delete_database():
    #perform deletion
    print('Database deleted!')

def check_permission(func):
    def secure_deletion():
        if user.get('role') == 'admin':
            return func()
        else:
            raise PermissionError('You are not an admin bro!')
    return secure_deletion

secure_delete_database = check_permission(delete_database)

secure_delete_database()        
