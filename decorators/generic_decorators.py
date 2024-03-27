import functools

user = {'username': 'feri124', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)  #to make sure that the inner only works as a wrapper so e.g __name__ will be the actual function name, not the secure_func
    def secure_function(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
    return secure_function
    

@user_has_permission
def my_function(panel):
    return f'Admin password for {panel} panel is pwd1234.'


#end goal: user_has_permission('admin')(my_function)
print(my_function('movies'))