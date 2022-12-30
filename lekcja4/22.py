arr=[4,36,12,28,9,44,5]
arr1=[5,1,36]
x=[arr+arr1]
for element in arr1:
    if element in arr:
        arr.remove(element)
print(arr)
