import random
class arrays():
    @staticmethod
    def method_name(number,value):
        a=[]
        for i in range(number):
            a.append(value)
        return a
    @staticmethod
    def randoms(number,m,n):
        arr=[]
        for i in range(number):
            arr.append(random.randint(m,n))
        return arr
    @staticmethod
    def method(element,x,y):
        arr=[]
        for i in range(element):
            arr.append





p=arrays.method_name(5,8)
y=arrays.randoms(10,0,5)
print(p,y)