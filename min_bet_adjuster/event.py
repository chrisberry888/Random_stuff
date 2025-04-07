from typing import List 
import random
from outcome import Outcome

class Event:
    
    def __init__(self, outcome_names: List[str],
                 outcome_probabilities: List[float],
                 outcome_popularities: List[float],
                 outcome_starting_balance: List[float]):
        self.outcome_names = outcome_names
        self.outcome_probabilities = outcome_probabilities
        self.outcome_popularities = outcome_popularities
        self.outcome_starting_balance = outcome_starting_balance
        self.outcomes = []

        for i, outcome in enumerate(outcome_names):
            next_outcome = Outcome(
                name=outcome_names[i],
                probability_of_occuring=outcome_probabilities[i],
                popularity_percent=outcome_popularities[i],
                money_on_outcome=outcome_starting_balance[i]
            )
            self.outcomes.append(next_outcome)