arr=[32,4,5,67,2,6,7,3,5,76,8]
arr2=[4,57,4,6,78,6,544,6,7]
for i in arr:
        if i in arr2:
            x=1
        else:
            x=0
if x==1:
    print("arraye są równe")
else:
    print("arraye nie są równe")
