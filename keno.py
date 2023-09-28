#Calculating the house edge/EV of keno
#Calculations based on $1 bet per game (or $2 if bonus is bought)
import math

def keno(spots, bonus):
    pay_tables = {
        1: {
            1: 2.5
        },
        2: {
            1: 1,
            2: 5
        },
        3: {
            2: 2.5,
            3: 25
        },
        4: {
            2: 1,
            3: 4,
            4: 100
        },
        5: {
            3: 2,
            4: 20,
            5: 450
        },
        6: {
            3: 1,
            4: 7,
            5: 50,
            6: 1600
        },
        7: {
            3: 1,
            4: 3,
            5: 20,
            6: 100,
            7: 5000
        },
        8: {
            4: 2,
            5: 10,
            6: 50,
            7: 1000,
            8: 15000
        },
        9: {
            4: 1,
            5: 5,
            6: 25,
            7: 200,
            8: 4000,
            9: 40000
        },
        10: {
            0: 2,
            5: 2,
            6: 20,
            7: 80,
            8: 500,
            9: 10000,
            10: 100000
        },
        11: {
            0: 2,
            5: 1,
            6: 10,
            7: 50,
            8: 250,
            9: 1500,
            10: 15000,
            11: 500000
        },
        12: {
            0: 4,
            6: 5,
            7: 25,
            8: 150,
            9: 1000,
            10: 2500,
            11: 25000,
            12: 1000000
        }
    }
    
    total_tickets = math.comb(80, spots)
    winners = []
    winners_value = []
    for key in pay_tables[spots]:
        winning_tix = math.comb(20, key) * math.comb(60, spots-key)
        winners.append(winning_tix)
        winners_value.append(winning_tix * pay_tables[spots][key])
    
    
    win_percent = round(total_tickets/sum(winners), 2)
    EV_of_one_card = round(sum(winners_value)/total_tickets, 4)
    return [win_percent, EV_of_one_card]
    

header = ["Spots", "Win Percentage", "Value of one card", "(No Bonus)"]
print(f"{header[0]:<8} {header[1]:<16} {header[2]:<20} {header[3]:<11}")
for i in range(1, 13):
    temp = keno(i, False)
    print(f"{i:<8} 1:{temp[0]:<14} {temp[1]:<20}")