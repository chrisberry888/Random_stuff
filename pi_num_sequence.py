#This lists the sequence of numbers n such that there exist numbers a and be where  
#a+b=n and a/b is a better approximation of pi (or e) (or any other number than the previous n.
import math

n = 1
last_n = 1
a = 0
b = 1
pi = math.e
diff = math.e
print(n)

for i in range(5000):
    n += 1
    for j in range(n-1):
        if abs(pi - (j + 1)/(n - (j + 1))) < diff:
            
            diff = abs(pi - float((j + 1)/(n - (j + 1))))
            
            a = j+1
            b = n-a
            
            print("%d,   %f,    %d,    %d,    %f" % (n,diff,a,b,(a/b)))
            break