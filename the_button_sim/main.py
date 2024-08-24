from Game_obj import Game

first_game = Game()

for i in range(10000):
    first_game.push_button()

print(f"Max Value: {first_game.max_value}")
print(f"Total Presses: {first_game.total_presses}")
print(f"Total Resets: {first_game.total_resets}")