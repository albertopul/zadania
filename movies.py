from operator import itemgetter, attrgetter
import random
from datetime import datetime


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
   
def generate_views():
    movie_count = 8
    for i in range(movie_count):
        idx = random.randint(0, len(main_list)-1)
        main_list[idx].plays = main_list[idx].plays + random.choice(range(1,100))
    print(f"{main_list[idx].title} {main_list[idx].year} played {main_list[idx].plays} times")

def generate_view(times = 10):
    for i in range(times):
        generate_views()

def top_titles():
    print(f"Most viewed movies and series today ({datetime.today().strftime('%Y-%m-%d  %H:%M:%S')})")
    x =  int(input("How many Top movies and series would you like to see? "))
    by_plays = (sorted(main_list, key=lambda item: item.plays, reverse=True))
    top_list= by_plays[0:x]
    for item in top_list:
        if isinstance(item, Movie) == True:
            print(f"{item.title} {item.year} played {item.plays} times")
        if isinstance(item, Series) == True:
            print(f"{item.title} {item.year} S{item.season}E{item.episode} played {item.plays} times")   


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
generate_view()
print()
top_titles()