from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.review import Review
from datetime import datetime

import pytest

@pytest.fixture()
def review():
    return Review(Movie("", 0),"",0)

def test_init(review):
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = 8
    review = Review(movie, review_text, rating)

    ## test cr3
    assert repr(review.movie) == "<Movie Moana, 2016>"
    assert "Review: {}".format(review.review_text) == "Review: This movie was very enjoyable."
    assert "Rating: {}".format(review.rating) == "Rating: 8"

    ##test movie
    actor = Actor("Will Smith")
    review.movie = actor ##illegal
    assert repr(review.movie) == "<Movie Moana, 2016>"
    movie = Movie("Will Smith smith Will Smith?", 1900)
    review.movie = movie  ##legal
    assert repr(review.movie) == "<Movie Will Smith smith Will Smith?, 1900>"

    ##test review text
    review.review_text = 1900 ##illegal
    assert review.review_text == "This movie was very enjoyable."
    review.review_text = "Will Smith will smith Will Smith" ##legal
    assert review.review_text == "Will Smith will smith Will Smith"

    ##test rating
    review.rating = 10.1
    assert review.rating == 8
    review.rating = 9
    assert review.rating == 9

    ##test __eq__
    movie = Movie("Will Smith smith Will Smith?", 1900)
    review_text = "Will Smith will smith Will Smith"
    rating = 9
    review1 = Review(movie, review_text, rating)
    assert review == review1




