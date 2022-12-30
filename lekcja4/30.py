def minmax(array):
    max=0
    min=10
    for i in array:
        if i>max:
            max=i
    for j in array:
        if j<min:
            min=j
    return min,max

print(minmax([4,2,8,4,7,9,5]))
