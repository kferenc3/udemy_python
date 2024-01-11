MENU_PROMPT = """
------------------------
AwesomeMovieDatabase3000
------------------------

Please select an option:
    - Type 'a' for adding a new movie,
    - Type 'l' for listing all movies,
    - Type 'f' to find a movie in the database,
    - Type 'q' to quit,
"""
movies = []

def addmovie(movielist):
    title = input('Enter the movie title:').title()
    director = input('Enter the director of the movie:').title()
    year = input('Enter the release year of the movie:')
    while True:
        try:
            int(year)
        except ValueError:
            print("The year should be a valid number. Please try again:")
            year = input('Enter the release year of the movie:')
        else:
            break
    movielist.append({'title': title, 'director': director, 'rel_year': year})

def findmovie(searchstr, movielist):
    for movie in movielist:
        if movie['title'].lower() == searchstr.strip().lower():
            return movie
        else:
            return None

def printmovie(mov):
    print(f"Title: {mov['title']}\nDirector: {mov['director']}\nRelease year: {mov['rel_year']}\n")

opt = input(MENU_PROMPT).lower()
while opt != 'q':
    if opt == 'a':
        addmovie(movies)
    elif opt == 'l':
        for movie in movies:
            printmovie(movie)
    elif opt == 'f':
        search = input("Enter the movie's title you wish to find in the database:")
        result = findmovie(search, movies)
        if result:
            printmovie(result)
        else:
            print("The requested movie is not found.")
    elif opt not in ['a','l','f','q']:
        print('\nINVALID OPTION!')
    opt = input(MENU_PROMPT).lower()