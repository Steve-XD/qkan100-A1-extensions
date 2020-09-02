from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User

import pytest

@pytest.fixture()
def user():
    return User("","")

def test_init(user):
    #test cr3
    user1 = User('Martin', 'pw12345')
    user2 = User('Ian', 'pw67890')
    user3 = User('Daniel', 'pw87465')
    assert repr(user1) == "<User martin>"
    assert repr(user2) == "<User ian>"
    assert repr(user3) == "<User daniel>"

    #test user_name
    assert user1.user_name == "martin"
    user1.user_name = 900 ##illegal
    assert user1.user_name == "martin"
    user1.user_name = " STEVEN " ##legal
    assert user1.user_name == "steven"

    #test password
    assert user1.password == 'pw12345'
    user1.password = 900  ##illegal
    assert user1.password == 'pw12345'
    user1.password = "pv wej asd 123" ##legal
    assert user1.password == "pv wej asd 123"

    #test watched_movie
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 178
    movie2 = Movie("My life is a Legend!", 1905)
    movie2.runtime_minutes = 2000
    user1.watch_movie(movie1) ##legal
    user1.watch_movie(movie2)
    assert str(user1.watched_movies) == "[<Movie Moana, 2016>, <Movie My life is a Legend!, 1905>]"
    review1 = Review(movie1, "Fantastic movie", 9)
    user1.watch_movie(review1) ##illegal
    assert str(user1.watched_movies) == "[<Movie Moana, 2016>, <Movie My life is a Legend!, 1905>]"
    user1.watched_movies = movie1
    assert str(user1.watched_movies) == "[<Movie Moana, 2016>]"
    user1.watched_movies = review1
    assert str(user1.watched_movies) == "[<Movie Moana, 2016>]"

    # test reviews
    review2 = Review(movie2, "Horrible movie", 3)
    user1.add_review(review1) ##legal
    user1.add_review(review2)
    assert str(user1.reviews) == "[<Review (9/10):Fantastic movie>, <Review (3/10):Horrible movie>]"
    user1.add_review(movie1) ##illegal
    assert str(user1.reviews) == "[<Review (9/10):Fantastic movie>, <Review (3/10):Horrible movie>]"
    user1.reviews = review1 ##legal
    assert str(user1.reviews) == "[<Review (9/10):Fantastic movie>]"
    user1.reviews = movie2 ##illegal
    assert str(user1.reviews) == "[<Review (9/10):Fantastic movie>]"

    # test time_spent_watching_movies_minutes
    assert user1.time_spent_watching_movies_minutes == 2178
    user1.time_spent_watching_movies_minutes = 2000  #LEGAL
    assert user1.time_spent_watching_movies_minutes == 2000
    user1.time_spent_watching_movies_minutes = -1 #illegal
    assert user1.time_spent_watching_movies_minutes == 2000

    ## test __eq__
    user4 = User('SteVen', '1561')
    assert user1 == user4

    ## test __lt__
    a_list = [user1, user2, user3]
    assert str(a_list) == "[<User steven>, <User ian>, <User daniel>]"
    a_list.sort()
    assert str(a_list) == "[<User daniel>, <User ian>, <User steven>]"

    ## test __hash__
    assert len({user1, user4}) == 1





