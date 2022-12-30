def f1(a):
    licnik=0
    for i in a:
        if i % 2 ==0 and i>8:
            licnik+=1
    return licnik



print(f1([3,543,7,8,543,3,78,324,3465,6779,435]))