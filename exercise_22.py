from functools import wraps

# DO NOT CHANGE
def get_current_user_role() -> int:
    # return the current user's role, represented by an int
    # for example, 0 - admin, 1 - user, 2 - guest
    # You don't need to change this function, we will replace it with a real function that returns the user's role
    return 0


def access_control(access_level: int):
    # You code starts here:
    def check_access(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if access_level <= get_current_user_role():
                return func(*args, **kwargs)
            else:
                raise PermissionError('You do not have the proper access level.')
        return wrapper
    return check_access
    
@access_control(0)
def delete_file(filename):
    #perform file deletion
    return f'{filename} has been deleted'

print(delete_file('text.txt'))