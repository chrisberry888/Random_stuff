from random import randint

class Game:
    def __init__(self):
        self.total_presses = 0
        self.total_resets = 0
        self.max_value = 0
        self.current_value = 0
        self.percent_prob_of_reset = 0

    def push_button(self):
        self.total_presses += 1
        if randint(1, 100) <= self.percent_prob_of_reset:
            self.reset()
        else:
            self.add_one()
    
    def reset(self):
        self.total_resets += 1
        self.current_value = 0
        self.percent_prob_of_reset = 0

    def add_one(self):
        self.current_value += 1
        self.percent_prob_of_reset += 1
        if self.current_value > self.max_value:
            self.max_value = self.current_value
