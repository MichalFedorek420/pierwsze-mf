import re
with open("grades2.txt","r") as f:
    x=re.findall(r'[0,9]+[0,9.]+',f.read())
    print(x)
    s=0
    for i in x:
        print(float(i)/len(x))

    
