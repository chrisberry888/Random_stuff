from dataclasses import dataclass, field
from typing import List
from bet import Bet

@dataclass
class Outcome:
    name: str
    current_odds: float = 1
    bets: List[Bet] = field(default_factory=list)

    def place_bet(self, amount):
        self.bets.append(Bet(amount_bet=amount,
                        odds=self.current_odds))
        

