arr=[5,1,9,6,1]
max=0
nd=0
for i in arr:
    if i>max:
        max=i
for i in arr:
    if max>i>nd:
        nd=i
print(nd)
