'''
I got an email from MathsGear about how 2026 can be written as the sum of 7 cubes in 9 different ways. 
They give one example (2026 = 1000 + 1000 + 8 + 8 + 8 + 1 + 1), then say that finding the remaining
combinations are left as an exercise to the reader. I am making this program to find these remaining 
combinations.

UPDATE: 7:46PM
I did it. The answers are:
2026 = 1000 + 1000 + 8 + 8 + 8 + 1 + 1
2026 = 1728 + 216 + 64 + 8 + 8 + 1 + 1
2026 = 729 + 729 + 512 + 27 + 27 + 1 + 1
2026 = 1000 + 729 + 216 + 64 + 8 + 8 + 1
2026 = 1331 + 512 + 64 + 64 + 27 + 27 + 1
2026 = 1000 + 343 + 216 + 216 + 125 + 125 + 1
2026 = 729 + 512 + 343 + 343 + 64 + 27 + 8
2026 = 1000 + 343 + 216 + 216 + 216 + 27 + 8
2026 = 729 + 729 + 216 + 216 + 64 + 64 + 8
'''

import sys

def get_cubes_list(num: int) -> list[int]:
    '''
    Takes any positive integer as input, and outputs the list of cubes smaller than it.
    
    :param num: Any integer greater than or equal to 1
    :type num: int
    :return: List of cube numbers less than or equal to num
    :rtype: list[int]
    '''
    cubes = []
    base_number = 1
    while base_number ** 3 <= num:
        cubes.append(base_number ** 3)
        base_number += 1
    return cubes


def get_cube_sums(num: int) -> tuple[list[int], list[list[int]]]:
    '''
    THIS DESCRIPTION IS WRONG BUT I'M TOO LAZY TO CHANGE IT
    Input: num = any integer > 1
    Output: tuple[list[int], list[list[int]]] = 
    A tuple: the first element is a list of cubes. The second element is a list of lists of integers, 
    with each sublist representing one sum of cubes that sums to num.
    
    Example:
    get_cube_sums(10) would return [[1,8], [[10,0],[2,1]]]
    Since 1 and 8 are the only two cubes that we'd need, and the only two ways of summing 10 using these
    two cubes is: 10 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1, or 10 = 1 + 1 + 8.
    '''

    cubes = get_cubes_list(num)
    list_of_cube_sums = []

    current_answer = [0 for i in range(len(cubes))]
    # for 



    print(cubes)
    pass


def cycle(current_list):
    '''
    I want to cycle through every list of 12 integers that sum to 7. 
    I manually iterated about 50 or so by hand in my notebook until I found a pattern.
    The pattern I found is thus:
    1) If the last cell is 0: subtract 1 from the rightmost nonzero cell, and add 1 to the cell directly
    to the right of it.
    2) If the last cell is non-zero: find the second-rightmost nonzero cell (A), add the contents of the last cell
    to cell A+1, change the contents of the last cell to 0, subtract 1 from A, then add 1 to A+1.

    Example:
    input1: [3, 1, 0, 3, 0]
    output1: [3, 1, 0, 2, 1]

    input2: [2, 2, 0, 0, 3]
    output2: [2, 1, 4, 0, 0]
    
    :param current_list: Description
    '''
    addend = current_list[-1]
    current_list[-1] = 0
    for i, number in reversed(list(enumerate(current_list))):
        if number != 0:
            current_list[i] -= 1
            current_list[i+1] = 1 + addend
            return
        

def dot(list1, list2):
    '''
    Dot product between list1 and list2.

    Ripped this directly from stackoverflow
    '''
    if len(list1) != len(list2):
        return 0
    return sum((i[0] * i[1] for i in zip(list1, list2)))


def make_strings(big_num, list_of_lists, cubes):
    final_strings = []
    for current_list in list_of_lists:
        answer = f'{big_num} ='
        for i, cube in reversed(list(enumerate(cubes))):
            while current_list[i] != 0:
                answer += f" {cube} +"
                current_list[i] -= 1
        final_strings.append(answer[:-2])

    return final_strings
    


def hyperspecific():
    final_list = []
    cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728]
    current_answer = [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    last_answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]
    while current_answer != last_answer:
        if dot(cubes, current_answer) == 2026:
            final_list.append(current_answer.copy())
        cycle(current_answer)


    for my_string in make_strings(2026, final_list, cubes):
        print(my_string)



def main():
    hyperspecific()

if __name__ == "__main__":
    main()