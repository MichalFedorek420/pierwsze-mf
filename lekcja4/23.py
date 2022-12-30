def bubblesort(arr):
    n=len(arr)
    while n>1:
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]=arr[i+1],arr[i]
        n-=1
    return arr
print(bubblesort([8,9,67,6,23]))




