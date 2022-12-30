import random
def rand_elem(array):
    return array[random.randrange(0,len(array))]
print(rand_elem([1,2,3,4]))