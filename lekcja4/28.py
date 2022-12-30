# def median(array):
#         x=len(array)/2
#         return(array[x])
# print(median([1,0,9,4,6,]))
def median(array):
    for i in range(len(array)):
        for j in range(len(array)):
            x=
            if array[i] < array[j]:
                array[j],array[i] = array[i],array[j]
    return array, array[x]

listToSort = [22,11,23,1,100,24,3,101,2,4]
print(median(listToSort))