from re import X


x= int(input("podaj x: "))
y = int(input("podaj y: "))

if x>0 and y>0:
    print("first quarter")
if x>0 and y<0:
    print("fourth quarter")
if x<0 and y<0:
    print("third quarte")
if x<0 and y>0:
    print("second quarter")


