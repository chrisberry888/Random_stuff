from random import randint
from session_obj import Session

class Game:
    def __init__(self):
        self.total_presses = 0
        self.total_resets = 0
        self.max_value = 0
        self.current_session = Session()
        self.presses_to_new_max = [0]

    def push_button(self):
        self.total_presses += 1
        if self.current_session.push_button():
            self.adjust_max()
        else:
            self.reset()
    
    def adjust_max(self):
        if self.current_session.current_value > self.max_value:
            self.max_value = self.current_session.current_value
            self.presses_to_new_max.append(self.total_presses)

    def reset(self):
        self.total_resets += 1
        self.current_session = Session()

    def report_stats(self):
        output = ""
        output += (f"Max Value: {self.max_value}\n")
        output += (f"Total Presses: {self.total_presses}\n")
        output += (f"Total Resets: {self.total_resets}\n")

        i = 0
        for value in self.presses_to_new_max:
            output += (f"Presses to {i}: {value}\n")
            i += 1
        
        return output
