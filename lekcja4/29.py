arr=[5,6,5,78,43,67,546,134,86,354,2345,22,67,89,1,3,10]
x=int(input("podaj dowolną liczbę: "))
l=[]
for i in arr:
    if i>x:
        l.append(i)
print(l)
