import functools

user = {'username': 'feri124', 'access_level': 'guest'}

def user_has_permission(func):
    @functools.wraps(func)  #to make sure that the inner only works as a wrapper so e.g __name__ will be the actual function name, not the secure_func
    def secure_function():
        if user.get('access_level') == 'admin':
            return func()
    return secure_function

@user_has_permission
def my_function():
    return 'Admin password is pwd1234.'



print(my_function())