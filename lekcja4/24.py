arr=[3,5,6,7,8,2,1,3,5,7,0,9,87,54,3]
x=[]
for i in arr:
    if arr.count(i) == 1:
        x.append(i)

print(x)