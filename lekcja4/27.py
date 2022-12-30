arr=[5,1,9,6,1]
max=0
min=10
for i in arr:
    if i>max:
        max=i
for j in arr:
    if j<min:
        min=j
print(max-min)