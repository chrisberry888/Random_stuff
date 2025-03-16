'''I Started writing this python program that translated different gambling odds.
Stopping after half an hour because I'm bored with it. I may return to it but probably not.
'''

#function that takes american odds and translates them into european odds and implied percentages
#function that takes european odds and translates them into american odds and implied percentages
#function that takes a percentage value and translates it into american and european odds
#driver function

def percentage_odds_translator(percentage):
    if percentage >= 1 or percentage <= 0:
        print("Invalid input: percentage must be betweeen 0 and 1 (exclusive)")
        return {}
    return_value = {"Implied Percentage": percentage}
    american_odds = 

def correct_sign(odds):
    sign = "+" if odds >= 0 else "-"
    return sign

def american_odds_translator(odds):
    if odds < 100 and odds > -100:
        print("Invalid input: American odds must be either less than -100 or greater than 100")
        return False
    numerator = 100 if odds >= 100 else abs(odds)
    implied_percentage = numerator / (100 + abs(odds))
    european_odds = 1 + (odds / 100 if odds >= 100 else 100 / abs(odds))
    fractional_odds = f"{odds / 100} to 1" if odds >= 100 else f"1 to {abs(odds) / 100}"
    print(f"American Odds: {correct_sign(odds)}{abs(odds)}")
    print(f"Decimal Odds: {european_odds}")
    print(f"Fractional Odds: {fractional_odds}")
    print(f"Implied Percentage: {implied_percentage}")
    return True

def decimal_odds_translator(odds):
    if odds <= 1:
        print("Invalid input: Decimal (European) odds must be greater than 1")
        return False
    american_odds = (odds - 1) * 100 if odds >= 2 else -100 / (odds - 1)
    implied_percentage =
user_input = input("Enter a number: ")
american_odds_translator(int(user_input))