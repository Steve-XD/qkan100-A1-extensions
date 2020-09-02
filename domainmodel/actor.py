"""
Name: Qi Wen Kan
UPI: qkan100
"""
class Actor:

    def __init__(self, actor_full_name : str):
        self.colleagues = []

        if actor_full_name  == "" or type(actor_full_name ) is not str:
            self.__actor_full_name  = None
        else:
            self.__actor_full_name  = actor_full_name .strip()

    @property
    def actor_full_name (self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.__actor_full_name  == other.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name  < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name )

    def add_actor_colleague(self, other):
        self.colleagues.append(other)

    def check_if_this_actor_worked_with(self, other):
        return other in self.colleagues





