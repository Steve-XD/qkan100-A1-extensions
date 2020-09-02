"""
Name: Qi Wen Kan
UPI: qkan100
"""
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, title : str, year : int):
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__rank = None
        self.__rating = None
        self.__votes = None
        self.__revenue_millions = None
        self.__metascore = None
        if title == "" or type(title) is not str or year < 1900 or type(year ) is not int:
            self.__title   = None
            self.__year = None
        else:
            self.__title = title.strip()
            self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def director(self):
        return self.__director

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @title.setter
    def title(self, title):
        if title != "" and type(title) is str:
            self.__title = title.strip()

    @description.setter
    def description(self, description):
        if description != "" and type(description) is str:
            self.__description = description.strip()

    @director.setter
    def director(self, director):
        if isinstance(director, Director):
            self.__director = director

    @actors.setter
    def actors(self, actor):
        if isinstance(actor, Actor):
            self.__actors = [actor]

    @genres.setter
    def genres(self, genre):
        if isinstance(genre, Genre):
            self.__genres = [genre]

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is int and runtime_minutes > 0:
            self.__runtime_minutes = runtime_minutes
        else:
            raise ValueError("ValueError exception thrown")

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        return self.__title  == other.__title and self.__year == other.__year

    def __lt__(self, other):
        return (self.__title, self.__year) < (other.__title, other.__year)

    def __hash__(self):
        return hash((self.__title, self.__year))

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if isinstance(actor, Actor) and actor in self.__actors:
            self.__actors.pop(self.__actors.index(actor))

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if isinstance(genre, Genre) and genre in self.__genres:
            self.__genres.pop(self.__genres.index(genre))

    ###################################### extension ######################################
    @property
    def year(self):
        return self.__year

    @property
    def rank(self):
        return self.__rank

    @property
    def rating(self):
        return self.__rating

    @property
    def votes(self):
        return self.__votes

    @property
    def revenue_millions(self):
        return self.__revenue_millions

    @property
    def metascore(self):
        return self.__metascore

    @year.setter
    def year(self, year):
        if type(year) is int and year >= 1900:
            self.__year = year
        else:
            raise ValueError("ValueError exception thrown")

    @rank.setter
    def rank(self, rank):
        if type(rank) is int and rank >= 0:
            self.__rank = rank
        else:
            raise ValueError("ValueError exception thrown")

    @rating.setter
    def rating(self, rating):
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            raise ValueError("ValueError exception thrown")

    @votes.setter
    def votes(self, votes):
        if type(votes) is int and votes >= 0:
            self.__votes = votes
        else:
            raise ValueError("ValueError exception thrown")

    @revenue_millions.setter
    def revenue_millions(self, revenue_millions):
        if revenue_millions == "N/A":
            self.__revenue_millions = "N/A"
        elif float(revenue_millions) >= 0:
            self.__revenue_millions = float(revenue_millions)
        else:
            raise ValueError("ValueError exception thrown")

    @metascore.setter
    def metascore(self, metascore):
        if metascore == "N/A":
            self.__metascore = "N/A"
        elif 0 <= float(metascore) <= 100:
            self.__metascore = float(metascore)
        else:
            raise ValueError("ValueError exception thrown")






