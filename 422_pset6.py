def hw_prob():
    points = [[1/(401**.5), 20/(401**.5)], [-1/(10**.5), 3/(10**.5)]]
    labels = [1,-1]
    weights = [0,0]
    nothing_changed = False
    epochs = 0
    while(not nothing_changed):
        nothing_changed = True
        epochs += 1
        for i in range(len(points)):
            temp = 0
            for j in range(len(weights)):
                temp += points[i][j]*weights[j]
            if temp*labels[i] <= 0:
                nothing_changed = False
                for j in range(len(weights)):
                    weights[j] += points[i][j]*labels[i]
        print(weights)
    epochs -= 1
    print(epochs)
    
hw_prob()