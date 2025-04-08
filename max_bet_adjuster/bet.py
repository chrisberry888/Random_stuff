from dataclasses import dataclass, field
from typing import List

@dataclass
class Bet:
    amount_bet: float
    odds: float # European odds (aka decimal odds)

    def payout(self) -> float:
        return self.amount_bet * self.odds