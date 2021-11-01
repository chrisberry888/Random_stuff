#this whole program describes every septatonic scale containing only major and minor thirds.


def is_valid(arr):
    if sum(arr) != 12:
        return False
    if arr[0] + arr[-1] != 3 and arr[0] + arr[-1] != 4:
        return False
    for i in range(len(arr)-1):
        if arr[i] + arr[i+1] != 3 and arr[i] + arr[i+1] != 4:
            return False
    return True
    
    
scale = [1 for i in range(7)]
end = [3 for i in range(7)]

while scale != end:
    scale[0] += 1
    for i in range(len(scale)-1):
        if scale[i] == 4:
            scale[i] = 1
            scale[i+1] += 1
            
    if is_valid(scale):
        print(scale)
        