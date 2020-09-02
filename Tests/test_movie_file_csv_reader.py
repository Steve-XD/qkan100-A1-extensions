from domainmodel.movie import Movie
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader

import pytest

@pytest.fixture()
def movie_file_reader():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    return movie_file_reader

def test_init(movie_file_reader):
    movie_file_reader.read_csv_file()

    ## check cr3
    assert len(movie_file_reader.dataset_of_movies) == 1000
    assert len(movie_file_reader.dataset_of_actors) == 1985
    assert len(movie_file_reader.dataset_of_directors) == 644
    assert len(movie_file_reader.dataset_of_genres) == 20

    ## check director
    movie1 = Movie("Guardians of the Galaxy", 2014)
    assert movie_file_reader.dataset_of_movies[0].director == Director("James Gunn")

    ## check actors
    actors = "Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana".split(',')
    for i in range(len(actors)):
        actors[i] = Actor(actors[i])
    assert movie_file_reader.dataset_of_movies[0].actors == actors

    ## check genres
    movie2 = Movie("Jurassic World", 2015)
    genres = "Action,Adventure,Sci-Fi".split(',')
    for i in range(len(genres)):
        genres[i] = Genre(genres[i])
    assert movie_file_reader.dataset_of_movies[85].genres == genres

    ## check description
    assert movie_file_reader.dataset_of_movies[85].description == "A new theme park, built on the original site of Jurassic Park, creates a genetically modified hybrid dinosaur, which escapes containment and goes on a killing spree."

    ###################################### test extension ######################################

    ## check rank
    assert movie_file_reader.dataset_of_movies[85].rank == 86

    ## check rating
    assert movie_file_reader.dataset_of_movies[85].rating == 7

    ## check votes
    assert movie_file_reader.dataset_of_movies[85].votes == 455169

    ## check revenue_millions
    assert movie_file_reader.dataset_of_movies[85].revenue_millions == 652.18

    ## check metascore
    assert movie_file_reader.dataset_of_movies[85].metascore == 59

