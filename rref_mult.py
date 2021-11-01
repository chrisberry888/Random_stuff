def rref_mult(X,Y): #Takes 2 RREF matrices as input, outputs XY

    ans = zeroes(len(X),len(Y[0]))
    
    Xmarkers = [False for i in range(len(X))]
    Ymarkers = [False for i in range(len(Y))]
    
    #Finds the columns of X and Y where the pivots are, stores in X/Ymarkers
    i = 0
    for j in range(len(X[0])):
        if X[i,j] == 1:
            Xmarkers[j] = True
            i += 1
               
    i = 0
    for j in range(len(Y[0])):
        if Y[i,j] == 1:
            Ymarkers[j] = True
            i += 1
            
    
    for i in range(len(Xmarkers)):
        for j in range(len(Ymarkers)):
            curr = 0
            if Ymarkers[j]:
                ans[i,j] = X[i,curr]
                curr += 1
            else:
                ans[i,j] = Y[i,j]
    
    