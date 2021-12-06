def finder():
    maxim = 100
    a = []
    b = []
    for i in range(2, maxim):
        for j in range(1,i+1):
            if (i*i + j*j)%(i*j+1) == 0:
                a.append(i)
                b.append(j)
                
    print(a)
    print(b)
    
    num = []
    denom = []
    div = []
    
    for i in range(len(a)):
        num.append(a[i]**2 + b[i]**2)
        denom.append(a[i]*b[i] + 1)
        div.append(num[i]/denom[i])
    
    print(num)
    print(denom)
    print(div)
    
finder()
