def not_div(n):
    print("partial\ttotal")
    tot = 0
    temp = 0
    for i in range(100):
        if i%n == 0:
            tot += temp
            print("%d\t%d" % (temp, tot))
            temp = 0
        else:
            temp += i


not_div(4)
