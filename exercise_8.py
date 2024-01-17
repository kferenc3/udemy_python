class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

mymovie = Movie('Lord of the Rings', 'Peter Jackson')
print(mymovie.name)