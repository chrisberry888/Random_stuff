def collatz(n):
    steps = 0
    array = [n]
    while n != 1:
        steps += 1
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        array.append(n)
    print("STEPS: %d" % (steps))
    return array
    
c = collatz(63728127)

for num in c:
    print(num)