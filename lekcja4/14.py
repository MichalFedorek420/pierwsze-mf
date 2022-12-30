arr = [[True,False],[True,True],[False,False]]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==True:
            arr[i][j]=False
        else:
            arr[i][j]=True
print(arr)