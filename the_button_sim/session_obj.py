from random import randint

class Session:
    def __init__(self):
        self.is_alive = True
        self.current_value = 0
        self.percent_prob_of_reset = 0

    def push_button(self):
        if randint(1, 100) <= self.percent_prob_of_reset:
            self.is_alive = False
            return False
        else:
            self.current_value += 1
            self.percent_prob_of_reset += 1
            return True
    