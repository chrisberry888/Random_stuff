from typing import List 
import random
from outcome import Outcome

class Event:
    
    def __init__(self, outcome_names: List[str],
                 min_vig: float,
                 max_vig: float):
        self.outcomes = {}
        self.min_vig = min_vig
        self.max_vig = max_vig

        for outcome in outcome_names:
            self.outcomes[outcome] = Outcome(name=outcome,
                                             current_odds=1.9)

    def calculate_maximum_bet(self):
    