import functools

user = {'username': 'feri124', 'access_level': 'admin'}

def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)  #to make sure that the inner only works as a wrapper so e.g __name__ will be the actual function name, not the secure_func
        def secure_function(panel):
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_function
    return user_has_permission

@third_level('admin')
def my_function(panel):
    return f'Admin password for {panel} panel is pwd1234.'


#end goal: user_has_permission('admin')(my_function)
print(my_function('movies'))