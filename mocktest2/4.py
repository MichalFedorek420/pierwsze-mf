def f(dictionary,x,y):
    p=0
    for i in dictionary.values():
        for j in i:
            if j in range(x,y+1):
                p=p+j
    return p

    # for i in dictionary["arr1"]:
    #     if i in range(x,y+1):
    #         p=p+i
    # for j in dictionary["arr2"]:
    #     if j in range(x,y+1):
    #         p=p+i
    # return p
            
print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))