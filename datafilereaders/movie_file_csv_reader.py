"""
Name: Qi Wen Kan
UPI: qkan100
"""
import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []
        self.__dictionary_genres = {} ##extension
        self.__dictionary_actors = {} ##extension
        self.__dictionary_directors = {} ##extension

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            # index = 0
            for row in movie_file_reader:
                rank = int(row['Rank'])
                title = row['Title']
                release_year = int(row['Year'])
                actors = row['Actors'].split(',')
                director = Director(str(row['Director']))
                genres = row['Genre'].split(',')
                description = row['Description']
                runtime_minutes = int(row['Runtime (Minutes)'])
                rating = float(row['Rating'])
                votes = int(row['Votes'])
                revenue_millions = row['Revenue (Millions)']
                metascore = row['Metascore']

                ## create movie object
                movie = Movie(title, release_year)
                self.__dataset_of_movies.append(movie)

                ## add actors
                for actor in actors:
                    actor_obj = Actor(actor)
                    movie.add_actor(actor_obj)
                    if actor_obj not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actor_obj)
                        self.__dictionary_actors[actor_obj] = [movie]  ##extension
                    else:
                        self.__dictionary_actors[actor_obj].append(movie)  ##extension

                ## add director
                movie.director = director
                if director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(director)
                    self.__dictionary_directors[director] = [movie]  ##extension
                else:
                    self.__dictionary_directors[director].append(movie)

                ## add genre
                for genre in genres:
                    genre_obj = Genre(genre)
                    movie.add_genre(genre_obj)
                    if genre_obj not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genre_obj)
                        self.__dictionary_genres[genre_obj] = [movie] ##extension
                    else:
                        self.__dictionary_genres[genre_obj].append(movie) ##extension

                ## add description
                movie.description = description

                ## add runtime
                movie.runtime_minutes = runtime_minutes

                # print(f"Movie {index} with title: {title}, release year {release_year}")
                # index += 1

                ###################################### extension ######################################
                ## add rank
                movie.rank = rank

                ## add rating
                movie.rating = rating

                ## add votes
                movie.votes = votes

                ## add revenue_million
                movie.revenue_millions = revenue_millions

                ## add metascore
                movie.metascore = metascore

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    @property
    def dictionary_genres(self):
        return self.__dictionary_genres ##extension

    @property
    def dictionary_actors(self):
        return self.__dictionary_actors  ##extension

    @property
    def dictionary_directors(self):
        return self.__dictionary_directors  ##extension