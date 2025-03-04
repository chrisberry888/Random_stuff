from chord import Chord
from tuning import Tuning

def find_all_permutations(strings, fingers):
    '''
    Returns an array containing all possible permutations of "strings" strings
    being played using "fingers" fingers.
    '''
    permutations = []
    temp = [1,1,1,1]
    temp.extend(0 for i in range(strings-fingers))
    end = [0 for i in range(strings-fingers)]
    end.extend([1,1,1,1])

    permutations.append(temp.copy())
    
    while temp != end:
        temp[0] += 1
        for i in range(strings):
            if temp[i] > 1:
                temp[i] = 0
                temp[i+1] += 1
        if sum(temp) == 4:
            permutations.append(temp.copy())
    
    return permutations


def print_chords_with_root_as_lowest(permutation, tuning):
    pass

def print_all_chords(permutation, tuning):
    print_chords_with_root_as_lowest(permutation, tuning)


def guitar_chords_finder():
    tuning = Tuning.E_STANDARD.value
    strings = len(tuning)
    
    permutations = find_all_permutations(strings, 4)

    for permutation in permutations:
        print_all_chords(permutation, tuning)



