arr=[1,2,3,4,5]
arr[0]-=1
print(arr)
arr[-1]+=4
print(arr)
arr[int((len(arr)-1)/2)]=arr[int((len(arr)-1)/2)]*2
print(arr)
for n in range(len(arr)):
    arr[n]+=3
    print(arr)
