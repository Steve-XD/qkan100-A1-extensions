"""
Name: Qi Wen Kan
UPI: qkan100
"""
from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__movie = []


    def add_movie(self, movie):
        if movie not in self.__movie:
            self.__movie.append(movie)

    def remove_movie(self, movie):
        if movie in self.__movie and isinstance(movie, Movie):
            self.__movie.pop(self.__movie.index(movie))

    def select_movie_to_watch(self, index):
        if index < len(self.__movie):
            return self.__movie[index]
        else:
            return None

    def size(self):
        return len(self.__movie)

    def first_movie_in_watchlist(self):
        if self.__movie == []:
            return None
        else:
            return self.__movie[0]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__movie):
            self.__index += 1
            return self.__movie[self.__index - 1]
        else:
            raise StopIteration


