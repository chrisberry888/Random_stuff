
class Outcome:
    probability_of_occuring: float

    def __init__(self, probability_of_happening, popularity_percent):
        self.probability_of_occuring = probability_of_happening
        self.popularity_percent = popularity_percent

        