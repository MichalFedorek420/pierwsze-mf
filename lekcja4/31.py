arr=[324,45,6,2,6,8,45,2,7,89,3,34,7,57]
k=[]
for i in arr:
    if i % 2 == 0:
        k.append(i)
for i in arr:
    if i % 2 != 0:
        k.append(i)
print(k) 
