class MyError(Exception):
    """
    Example doc string
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

raise MyError('ouch', 500)
#print(err.__doc__)