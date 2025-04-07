from dataclasses import dataclass

@dataclass
class Outcome:
    name: str
    probability_of_occuring: float
    popularity_percent: float
    money_on_outcome: float

