"""
Name: Qi Wen Kan
UPI: qkan100
"""
from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, user_name, password):
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0
        if user_name == "" or type(user_name) is not str or password == "" or type(password) is not str:
            self.__user_name = None
            self.__password = None
        else:
            self.__user_name = user_name.strip().lower()
            self.__password = password

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password (self):
        return self.__password

    @property
    def watched_movies (self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @user_name.setter
    def user_name(self, user_name):
        if user_name != "" and type(user_name) is str:
            self.__user_name = user_name.strip().lower()

    @password.setter
    def password(self, password):
        if password != "" and type(password) is str:
            self.__password = password

    @watched_movies.setter
    def watched_movies(self, watched_movies):
        if isinstance(watched_movies, Movie):
            self.__watched_movies = [watched_movies]

    @reviews.setter
    def reviews(self, reviews):
        if isinstance(reviews, Review):
            self.__reviews = [reviews]

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent_watching_movies_minutes):
        if type(time_spent_watching_movies_minutes) is int and time_spent_watching_movies_minutes >= 0:
            self.__time_spent_watching_movies_minutes = time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if isinstance(movie, Movie):
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)

