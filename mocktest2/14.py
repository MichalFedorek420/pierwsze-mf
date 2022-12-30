def f4(d):
    y=0
    x=d.values()
    for i in x:
        for j in i:
            if j in range(5,10):
                y+=j
    return y

    
        
            


print(f4({"arr1":[2,6,5],"arr2":[7,1],"arr3":[2,9,8,1]}))