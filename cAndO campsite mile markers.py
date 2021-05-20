import re

strang = '''Mile 16.6 Swains Lock
Mile 26.1 Horsepen Branch
Mile 30.5 Chisel Branch
Mile 34.4 Turtle Run
Mile 38.2 Marble Quarry
Mile 42.5 Indian Flats
Mile 47.6 Calico Rocks
Mile 50.3 Bald Eagle Island
Mile 62.9 Huckleberry Hill
Mile 75.2 Killiansburg Cave
Mile 79.2 Horseshoe Bend
Mile 82.7 Big Woods
Mile 90.9 Opequon Junction
Mile 95.2 Cumberland Valley
Mile 101.2 Jordan Junction
Mile 110 North Mountain
Mile 116 Licking Creek
Mile 120.6 Little Pool
Mile 126.4 White Rock
Mile 129.9 Leopards Mill
Mile 133.6 Cacapon Junction
Mile 139.2 Indigo Neck
Mile 144.5 Devils Alley
Mile 149.4 Stickpile Hill
Mile 154.1 Sorrel Ridge
Mile 157.4 Purslane Run
Mile 162.1 Town Creek
Mile 164.8 Potomac Forks
Mile 169.1 Pigmans Ferry
Mile 175.3 Irons Mountain
Mile 180.1 Evitts Creek'''

x = strang.split("\n")
for lst in x:
    temp = lst.split()
    print(temp[1])
