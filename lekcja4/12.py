arr=[[2,5,4],[9,0,3]]
#a
print(arr)
#b
print(len(arr[0]),len(arr))
#c
print(arr[0][1])
#d
print(arr[1][2])
#e
print(arr[1])
#f
print(arr[0])
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if j==len(arr[i])-1:
            print(arr[i][j])
