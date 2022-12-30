arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if j==i:
            arr[i][j]=1
for a in arr:
    print(a)