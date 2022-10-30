def choose(a, b):
    res = 0
    for i in range()

#Calculates how much one powerball ticket is worth based on EV
#These are odds as of 10/30/22
def ticket_worth(jackpot):
    total_possibilities = 69*68*67*66*65*26
    prizes = [jackpot, 1000000, 50000, 100, 100, 7, 7, 4, 4]
    poss_for_each = [1, 25, 64, 64*25, 64*63, 64*63*25, 64*63*62, 64*63*62*61, 64*63*62*61*60]
    odds_for_each = [x/total_possibilities for x in poss_for_each]
    EV = 0
    for i in range(len(prizes)):
        EV += prizes[i] * odds_for_each[i]
        
    print(odds_for_each)
    
    return EV
    
print(ticket_worth(1000000000))