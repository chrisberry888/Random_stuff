'''
    I have a game on Steam called "THE BUTTON". The game is very simple: There is a button, and there 
    is a counter on the button that starts at 0. When that counter is 0, when you press the button,
    there is a 100% chance the counter goes to 1. When the counter is 1, there is a 99% chance it goes
    to 2, and a 1% chance it goes back to 0. When it's 2, there's a 98% chance it goes to the next 
    number and a 2% chance it resets to 0. And so on.

    I wasted about 2.5 hours on this game, and the highest number I got to was 37. My friend Dade played
    the game for 8 minutes and he got to 39.

    The purpose of this program is to find the probability of this happening (or the expected amount
    of time/button presses it would take to get to 39). I have written programs in the past that do
    something similar to this but I kind of just want to write redundant code right now.
'''

from random import random
from statistics import mean, median

def press_the_button(current_counter):
    rng = random() * 100
    return current_counter > rng
         

def press_button_through_one_cycle():
    counter = 0
    reset_to_0 = False
    while not reset_to_0:
        counter += 1
        reset_to_0 = press_the_button(counter)
    return counter

def run_simulation(number_to_reach):
    '''
    This function clicks the button until the number number_to_reach is reached.
    It returns the number on the button when the number is finally reached.
    '''
    
    total_button_presses = 0
    while True:
        number_reached = press_button_through_one_cycle()
        if number_reached >= number_to_reach:
            total_button_presses += number_to_reach
            return total_button_presses
        else:
            total_button_presses += number_reached


def run_dade_simulation(number_to_reach, max_button_presses):
    '''
    This function pushes the button until the number is reached, or the button has been
    pushed "max_button_presses" number of times.
    It returns True if the number is reached within max_button_presses, and False otherwise. 
    '''

    # If we have less than number_to_reach presses before we reach the number we want, logically 
    # we won't be able to reach the number by max_button_presses.
    real_max_presses = max_button_presses - number_to_reach
    total_button_presses = 0
    while total_button_presses <= real_max_presses:
        number_reached = press_button_through_one_cycle()
        if number_reached >= number_to_reach:
            return True
        else:
            total_button_presses += number_reached
    return False

def main():
    # presses_per_sim = []
    # for i in range(1000):
    #     presses_per_sim.append(run_simulation(39))

    # print('Average presses to get to 39:')
    # print(f'Mean: {mean(presses_per_sim)}')
    # print(f'Median: {median(presses_per_sim)}')

    dade_level_runs = 0
    dade_sims = 1000000
    number_to_reach = 39
    max_button_presses = 600
    for i in range(dade_sims):
        if run_dade_simulation(number_to_reach, max_button_presses):
            dade_level_runs += 1

    probability = dade_level_runs / dade_sims
    print(f'Probability of getting a Dade-run: {probability * 100}%')

if __name__ == "__main__":
    main()