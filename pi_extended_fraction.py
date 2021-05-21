#Generates the extended fraction addends for pi.
import math


def pi_extended_fraction():
    pi = math.pi
    floor = math.floor(pi)
    for i in range(100):
        print(floor)
        pi = 1/(pi - float(floor))
        floor = math.floor(pi)
        
#pi_extended_fraction()

print("%.50f" % math.pi)