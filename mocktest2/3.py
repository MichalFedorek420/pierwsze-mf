def f(array2d):
    array1d=[]
    a=0
    for i in range(len(array2d[0])):
        for j in range(len(array2d)):
            a+=array2d[j][i]
        array1d.append(a)
        a=0
    return(array1d)

    
print(f([[3,6,2,7],[9,5,4,0],[2,8,0,9]]))