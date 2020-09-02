"""
Name: Qi Wen Kan
UPI: qkan100
"""
from datetime import datetime

from domainmodel.movie import Movie


class Review:
    def __init__(self, movie, review_text: str, rating: int):
        if isinstance(movie, Movie) == False or review_text == "" or type(review_text) is not str or rating > 10 or rating < 1 or type(rating) is not int:
            self.__movie = None
            self.__review_text = None
            self.__rating = None
            self.__timestamp = None
        else:
            self.__movie = movie
            self.__review_text = review_text.strip()
            self.__rating = rating
            self.__timestamp = datetime.today()

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self.__movie = movie

    @review_text.setter
    def review_text(self, review_text):
        if review_text != "" and type(review_text) is str:
            self.__review_text = review_text.strip()

    @rating.setter
    def rating(self, rating):
        if type(rating) is int and 1 <= rating <= 10:
            self.__rating = rating

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp

    def __repr__(self):
        return f"<Review ({self.__rating}/10):{self.__review_text}>"

    def __eq__(self, other):
        return self.__movie == other.__movie and self.__review_text == other.__review_text and \
               self.__rating == other.__rating and self.__timestamp == other.__timestamp



