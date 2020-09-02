"""
Name: Qi Wen Kan
UPI: qkan100
"""
from domainmodel.movie import Movie
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User
from domainmodel.review import Review

class MovieWatchingSimulation:
    def __init__(self, existing_user, movie_file_reader):
        self.__existing_user = existing_user
        self.__movie_list = movie_file_reader.dataset_of_movies
        self.__genre_list = movie_file_reader.dataset_of_genres
        self.__genre_dict = movie_file_reader.dictionary_genres
        self.__director_list = movie_file_reader.dataset_of_directors
        self.__director_dict = movie_file_reader.dictionary_directors
        self.__actor_list = movie_file_reader.dataset_of_actors
        self.__actor_dict = movie_file_reader.dictionary_actors

    @property
    def existing_user(self):
        return self.__existing_user

    def create_new_account(self):
        username = str(input("[Signed up] What's your username? : ")).strip()
        new_user = User(username, 'abc')
        while new_user in self.__existing_user or username == "":  ## username existed or blank
            if new_user in self.__existing_user:
                print("Opps look like we have the same username, please try again...")
            else:
                print("Please don't leave your username empty!")
            username = str(input("[Signed up] What's your username? : ")).strip()
            new_user = User(username, 'abc')
        new_password = str(input("[Signed up] What's your password? : "))
        while new_password == "":  ## blank password
            print("Please don't leave your password empty!")
            new_password = str(input("[Signed up] What's your password? : "))
        new_user.password = new_password
        self.__existing_user.append(new_user)

    def existing_account(self):
        username = str(input("[Sign in] What's your username? : ")).strip()
        check_username = User(username, "abc")
        if check_username not in self.__existing_user: ## user doesn't exist
            print("Username does not exist!")
            return User("","")
        else:
            current_user = self.__existing_user[self.__existing_user.index(check_username)]
            current_password = str(input("[Sign in] What's your password? : "))
            while current_password != current_user.password:
                print("Password is not correct, please try again!")
                current_password = str(input("[Sign in] What's your password? : "))
            return current_user

    def homepage(self):
        print("Which movie would you like to watch today ?")
        print("-----------------------------------------------")
        print("1: Recommendation")
        print("2: Search by movie's title and year")
        print("3: Search by genre")
        print("4: Search by actor")
        print("5: Search by director")
        print("9: Logout")
        result = int(input("Press a number to choose your option: "))
        return result

    def review(self, movie):
        review_text = str(input("What you do want to say? : "))
        while review_text == "":
            print("You can't leave it blank!")
            review_text = str(input("What you do want to say? : "))

        rating = int(input("Rating out of 10? : "))
        while rating < 0 or rating > 10:
            print("Please rate between 0 to 10")
            rating = int(input("Rating out of 10? : "))
        return Review(movie, review_text, rating)

    def display_all_movie(self, movie_list, title):
        movie_index = 0
        options = 10
        choice = 1
        action = 0
        while action != 99:
            print("-----------------------------------------------")
            print(title)
            print("-----------------------------------------------")
            for movie in movie_list[movie_index:movie_index + options]:
                print("[{}] #{} {} ({}/10)".format(choice, movie.rank, movie.title, movie.rating))
                choice += 1
            if (movie_index - options) >= 0:
                print("[97] Previous")
            if (movie_index + options) < len(movie_list):
                print("[98] Next")
            print("[99] Back to homepage")
            action = int(input("Choose an option: "))
            if action == 97 and (movie_index - options) >= 0: ## previous option is selected
                movie_index -= options
            elif action == 98 and (movie_index + options) < len(movie_list): ## next option is selected
                movie_index += options
            elif action in [i+1 for i in range(choice)]:
                new_movie = movie_list[movie_index + action - 1]
                play = self.display_movie_details(new_movie)
                while play not in [1, 2, 3]:
                    print("Invalid input")
                    play = self.display_movie_details(new_movie)
                if play == 1:
                    return new_movie
                elif play == 2:
                    choice = 1
                    continue
                else:
                    return Movie("", 0)
            else:
                print("Invalid input!")
            choice = 1
        return Movie("",0)

    def display_movie_details(self, new_movie):
        print("-----------------------------------------------")
        print("Movie {}({})".format(new_movie.title, new_movie.year))
        print("-----------------------------------------------")
        print("Rank:", new_movie.rank, end=" | ")
        print("Rating: {}/10".format(new_movie.rating), end=" | ")
        print("Votes:", new_movie.votes, end = " | ")
        print("Metascore:", new_movie.metascore)
        print("Description:", new_movie.description)
        print("Director:", new_movie.director.director_full_name)
        print("Actors: ", end='')
        for actor in new_movie.actors:
            if actor != new_movie.actors[-1]:
                print(actor.actor_full_name, end=", ")
            else:
                print(actor.actor_full_name)
        print("Genres: ", end='')
        for genre in new_movie.genres:
            if genre != new_movie.genres[-1]:
                print(genre.genre_name, end=", ")
            else:
                print(genre.genre_name)
        if new_movie.runtime_minutes < 60:
            print("Runtime(min):", new_movie.runtime_minutes)
        else: #convert to hour and minutes
            hour = new_movie.runtime_minutes // 60
            minutes = new_movie.runtime_minutes % 60
            print("Runtime: {}h {}m".format(hour, minutes))
        print("Revenue (Millions):", new_movie.revenue_millions)
        print("-----------------------------------------------")
        print("1: Play")
        print("2: Back")
        print("3: Back to homepage")
        response = int(input("Press a number to choose your option: "))
        return response

    def show_recommendation(self): ##1
        movie = self.display_all_movie(self.__movie_list, "Recommendation")
        return movie

    def search_movie_title(self): ##2
        title = str(input("What's the movie's title? : "))
        year = int(input("What year did the movie release? : "))
        new_movie = Movie(title, year)

        while new_movie not in self.__movie_list:
            print("Oops movie not found...")
            action = str(input("Do you wish to try again? (Y/N) : ")).lower()
            if action == "y":
                title = str(input("What's the movie's title? : "))
                year = int(input("What year did the movie release? : "))
                new_movie = Movie(title, year)
            else:
                return Movie("",0)

        if new_movie in self.__movie_list:
            new_movie = self.__movie_list[self.__movie_list.index(new_movie)]
            play = self.display_movie_details(new_movie)
            while play not in [1,2,3]:
                print("Invalid input")
                play = self.display_movie_details(new_movie)
            if play == 1:
                return new_movie
            elif play == 2:
                return self.search_movie_title()
            else:
                return Movie("",0)

    def search_genre(self): ##3
        choice = 1
        action = 0
        while action != 99:
            print("-----------------------------------------------")
            print("Genres")
            print("-----------------------------------------------")
            for genre in self.__genre_dict:
                print("[{}] {} | ".format(choice, genre.genre_name), end='')
                choice += 1
                if choice % 7 == 0:
                    print('')
            print("[99] Back to homepage")
            action = int(input("Choose an option: "))
            if action in [(i + 1) for i in range(choice)]:
                movie_list = self.__genre_dict[self.__genre_list[action - 1]] ## open movie list according to genre
                title = "{} Movies".format(self.__genre_list[action - 1].genre_name)
                movie = self.display_all_movie(movie_list, title)
                return movie
            else:
                print("Invalid input!")
            choice = 1
        return Movie("", 0)

    def search_actor(self):  ##4
        actor = str(input("Who is the actor? : "))
        new_actor = Actor(actor)

        while new_actor not in self.__actor_list:
            print("Oops actor not found...")
            action = str(input("Do you wish to try again? (Y/N) : ")).lower()
            if action == "y":
                actor = str(input("Who is the actor? : "))
                new_actor = Actor(actor)
            else:
                return Movie("", 0)

        if new_actor in self.__actor_list:
            new_actor = self.__actor_list[self.__actor_list.index(new_actor)]
            movie = self.display_all_movie(self.__actor_dict[new_actor], "{}'s movie".format(new_actor.actor_full_name))
            return movie
        return Movie("", 0)

    def search_director(self):  ##5
        director = str(input("Who is the director? : "))
        new_director = Director(director)

        while new_director not in self.__director_list:
            print("Oops director not found...")
            action = str(input("Do you wish to try again? (Y/N) : ")).lower()
            if action == "y":
                director = str(input("Who is the director? : "))
                new_director = Director(director)
            else:
                return Movie("", 0)

        if new_director in self.__director_list:
            new_director = self.__director_list[self.__director_list.index(new_director)]
            movie = self.display_all_movie(self.__director_dict[new_director], "{}'s movie".format(new_director.director_full_name))
            return movie
        return Movie("", 0)

def main():
    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    existing_users = [User("Steven", "pass123")]
    gui = MovieWatchingSimulation(existing_users, movie_file_reader)
    while True:
        new = input("New to CS235Flix? (Y/N) : ").lower()
        if new == "y": ## create new account
            gui.create_new_account()
            existing_users = gui.existing_user
        else: ## sign in
            current_user = gui.existing_account()
            if current_user == User("",""):
                continue
            else:
                print("Logging in...")
                action = gui.homepage()
                while action != 9:
                    if action == 1: ## recommendation
                        movie = gui.show_recommendation()
                        if movie != Movie("",0):
                            current_user.watch_movie(movie)
                            print("You have watched", movie.title)
                            review = str(input("Do you want to give a review? (Y/N) : ")).lower()
                            if review == "y":
                                review = gui.review(movie)
                                current_user.add_review(review)
                        action = gui.homepage()
                    elif action == 2: ## search movie title and year
                        movie = gui.search_movie_title()
                        if movie != Movie("",0):
                            current_user.watch_movie(movie)
                            print("You have watched", movie.title)
                            review = str(input("Do you want to give a review? (Y/N) : ")).lower()
                            if review == "y":
                                review = gui.review(movie)
                                current_user.add_review(review)
                        action = gui.homepage()
                    elif action == 3: ## search movie by genre
                        movie = gui.search_genre()
                        if movie != Movie("",0):
                            current_user.watch_movie(movie)
                            print("You have watched", movie.title)
                            review = str(input("Do you want to give a review? (Y/N) : ")).lower()
                            if review == "y":
                                review = gui.review(movie)
                                current_user.add_review(review)
                        action = gui.homepage()
                    elif action == 4: ## search movie by actor
                        movie = gui.search_actor()
                        if movie != Movie("",0):
                            current_user.watch_movie(movie)
                            print("You have watched", movie.title)
                            review = str(input("Do you want to give a review? (Y/N) : ")).lower()
                            if review == "y":
                                review = gui.review(movie)
                                current_user.add_review(review)
                        action = gui.homepage()
                    elif action == 5: ## search movie by director
                        movie = gui.search_director()
                        if movie != Movie("",0):
                            current_user.watch_movie(movie)
                            print("You have watched", movie.title)
                            review = str(input("Do you want to give a review? (Y/N) : ")).lower()
                            if review == "y":
                                review = gui.review(movie)
                                current_user.add_review(review)
                        action = gui.homepage()
                    else:
                        action = gui.homepage()
                print("Logging out...")

main()
