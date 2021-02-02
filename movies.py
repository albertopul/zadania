from operator import itemgetter, attrgetter
import tabulate



class Movie:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays
        

    def play(self, step=1):
        self.plays += step
        return self.plays

    def __str__(self):
        return f'{self.title} ({self.year})'

    def __repr__(self):
        return f"Movie(title={self.title} year={self.year}, genre={self.genre}, plays={self.plays})"


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season}E{self.episode}'




def get_movies():
    movie_list = []
    for item in main_list:
        if isinstance(item, Series) == False:
            movie_list.append(item)
    movie_list_by_title = sorted(movie_list, key=lambda item: item.title)
    print("-------------------------------------------------------")
    print("This is a list of movies, sorted alphabetically:")
    print("-------------------------------------------------------")
    for item in movie_list_by_title:
        print(item)

def get_series():
    series_list = []
    for item in main_list:
        if isinstance(item, Series) == True:
            series_list.append(item)
    series_list_by_title = sorted(series_list, key=lambda item: item.title)
    print("------------------------------------------------------")
    print("This is a list of series, sorted alphabetically:")
    print("------------------------------------------------------")
    for item in series_list_by_title:
        print(item)

def search():
    print("-----------------------------------------------")
    search_result = []
    search_title = input("What title are you looking for? ")
    for item in main_list:
        if item.title == search_title:
            search_result.append(item)
    for item in search_result:
        print(item)
   
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# no i tu jest problem, bo nie wiem jak zrobić def generate_views()

# jeśli dobrze myślę, to top_titles() też nie zrobię póki nie mam generate_views()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

movie_one = Movie(title="Pulp Fiction", year="1994", genre="Crime", plays = 0)
movie_two = Movie(title="Crouching Tiger, Hidden Dragon", year="2000", genre="Fantasy", plays = 0)
movie_three = Movie(title="I'm Legend", year="2007", genre="Sci-fi", plays = 0)
movie_four = Movie(title="Gran Torino", year="2008", genre="Drama", plays = 0)
movie_five = Movie(title="The Green Mile", year="1999", genre="Drama", plays = 0)
serie_one = Series(title="The Flash", year="2014", genre="crime", season="01", episode="01", plays = 0)
serie_two = Series(title="The Flash", year="2014", genre="crime", season="01", episode="02", plays = 0)
serie_three = Series(title="The Flash", year="2015", genre="crime", season="02", episode="01", plays = 0)
serie_four = Series(title="The Flash", year="2015", genre="crime", season="02", episode="02", plays = 0)
serie_five = Series(title="The Arrow", year="2012", genre="crime", season="01", episode="01", plays = 0)
serie_six = Series(title="The Arrow", year="2012", genre="crime", season="01", episode="01", plays = 0)
serie_seven = Series(title="The Arrow", year="2013", genre="crime", season="02", episode="01", plays = 0)
serie_eight = Series(title="The Arrow", year="2013", genre="crime", season="02", episode="01", plays = 0)

main_list = [movie_one, movie_two, movie_three, movie_four, movie_five, serie_one, serie_two, serie_three, serie_four, serie_five, serie_six, serie_seven, serie_eight]
print("Biblioteka filmów")
print("----------------------")
for obj in main_list:
    print(obj)

print("----------------------")

print(movie_one)
movie_one.play()
print(f"{movie_one.title} played {movie_one.plays} times")
movie_one.play()
print(f"{movie_one.title} played {movie_one.plays} times")
serie_five.play()
print(f"{serie_five.title} S{serie_five.season}E{serie_five.episode} played {serie_five.plays} times")






get_movies()
print()
get_series()
print()
search()
print()



































"""
# CLASSES
# 2. Class for Movies:
class Movie:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        
        #Variables
        self.plays = plays
    
    def play(self, step=1):
        self.plays += step

    def __str__(self):
        return f'{self.title, self.year, self.genre, self.plays}'
    
    #def __repr__(self):
       # return 'Movie(title: %s, year: %s, genre: %s, plays: %r)' % (self.title, self.year, self.genre, self.plays)
    
    def movie_details(self):
        return f"{self.title} ({self.year})"

    def isSeries(self):
        return False
    
    def to_list(self):
        return [self.title, self.year, self.genre, self.plays]
    
    
# 3. Class for Series
class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"
    
    def __repr__(self):
        return f"Series(title:%s, year: %s, genre: %s, plays: %r, episode: %r, season: %r)" % (self.title, self.year, self.genre, self.plays, self.episode, self.season)

    def play(self, step=1):
        self.plays += step

    def isSeries(self):
        return True

    def to_list(self):
        return [self.title, self.year, self.genre, self.plays, self.season, self.episode]




movie_one = Movie(title="Pulp Fiction", year="1994", genre="Crime")
movie_two = Movie(title="Crouching Tiger, Hidden Dragon", year="2000", genre="Fantasy"),
movie_three = Movie(title="I'm Legend", year="2007", genre="Sci-fi"),
movie_four = Movie(title="Gran Torino", year="2008", genre="Drama"),
movie_five = Movie(title="The Green Mile", year="1999", genre="Drama"),
movie_six = Series(title="The Flash", year="2014", genre="crime", season="01", episode="01"),
serie_one = Series(title="The Flash", year="2014", genre="crime", season="01", episode="02"),
serie_two = Series(title="The Flash", year="2015", genre="crime", season="02", episode="01"),
serie_three = Series(title="The Flash", year="2015", genre="crime", season="02", episode="02"),
serie_four = Series(title="The Arrow", year="2012", genre="crime", season="01", episode="01"),
serie_five = Series(title="The Arrow", year="2012", genre="crime", season="01", episode="01"),
serie_six = Series(title="The Arrow", year="2013", genre="crime", season="02", episode="01"),
serie_seven = Series(title="The Arrow", year="2013", genre="crime", season="02", episode="01"),

main_list = [movie_one, movie_two, movie_three, movie_four, movie_five, movie_six, serie_one, serie_two, serie_three, serie_four, serie_five, serie_six, serie_seven]
for item in main_list:
    print(item)



# FUNCTIONS
# 3. Runs generate_movies and generate_series, returnig main_list.
def view_library(): 
    print(tabulate.tabulate(main_list, headers= ["Title", "Year", "Genre", "Plays", "Season", "Episode"]))
    

# 4. Runs generate_views() importing the main_list, then 
#    runs Movie.play(). Returns main_list

def generate_views(main_list):
    for item in main_list:
        Movie.play(item)
    return main_list

# 5. 1. get_movies takes the main_list, filters out only Class Movie() and
#    prints the resulting list in alphabetical order
    
def get_movies(main_list):
    movie_list = []
    for item in main_list:
        if item.isSeries() == False:
            movie_list.append(item)
    movie_list_by_title = sorted(movie_list, key=lambda item: item.title)
    movies_as_list = [m.to_list() for m in movie_list_by_title]
    print("-------------------------------------------------------")
    print("This is a list of your movies, sorted alphabetically:")
    print("-------------------------------------------------------")
    print(tabulate(movies_as_list, headers= ["Title", "Year", "Genre", "Plays"]))
  

# 5. 2. get_movies takes the main_list, filters out only Class Movie() and
#    prints the resulting list in alphabetical order    
def get_series(main_list):
    series_list = []
    for item in main_list:
        if item.isSeries() == True:
            series_list.append(item)
    series_list_by_title = sorted(series_list, key=lambda item: item.title)
    series_as_list = [n.to_list() for n in series_list_by_title]
    print("------------------------------------------------------")
    print("This is a list of your series, sorted alphabetically:")
    print("------------------------------------------------------")
    print(tabulate(series_as_list, headers= ["Title", "Year", "Genre", "Plays", "Season", "Episode"]))

    

# 6. Searches main_list for title and prints movie located on the main_list

def search(main_list):
    print("-----------------------------------------------")
    print(" Please choose a title from the lists above.")
    print("-----------------------------------------------")
    search_result = []
    search_title = input("What title are you looking for? ")
    for item in main_list:
        if item.title == search_title:
            search_result.append(item)
            
            if item.isSeries() == False:
                search_as_list = [o.to_list() for o in search_result]
                print(tabulate(search_as_list, headers= ["Title", "Year", "Genre", "Plays"]))

            elif item.isSeries() == True:
                search_as_list = [o.to_list() for o in search_result]
                print(tabulate(search_as_list, headers= ["Title", "Year", "Genre", "Plays", "Season", "Episode"]))


# 7. top_titels searches the top 'The' number of top titles. Takes 
#    variable 'The' from input and prints top_list.
def top_titles(main_list):
    print("Najpopularniejsze filmy i seriale dnia dzisiaj")
    for item in main_list:
        by_plays = (sorted(main_list, key=lambda item: item.plays, reverse=True))
    
    top_list= by_plays[0:The]
    
    top_as_list = [p.to_list() for p in top_list]
    print("------------------------------------")
    print("Here is your list, sorted by views:")
    print("------------------------------------")
    print(tabulate(top_as_list, headers= ["Title", "Year", "Genre", "Plays", "Season", "Episode"]))
 


if __name__ == "__main__":
    print("Biblioteka filmów")
    print("Generating movies and series data... please wait.")
  
    # Generate main_list:
    view_library()
    #print(main_list)
    

    # Generate views for plays in main_list:
    generate_views(main_list) 
    #print(main_list)
    
    # Get Movie tuples from main_list and transfer to movie_list,
    # sorted alphabetically by title.
    get_movies(main_list)
    print()
    
    # Get Series tuples from main_list and transfer to series_list,
    # sorted alphabetically by title.
    get_series(main_list)
    print()
    
    # Search the list for title.
    search(main_list)
    print()

    # Return a requested number of top titles.
    top_titles(main_list)
    """