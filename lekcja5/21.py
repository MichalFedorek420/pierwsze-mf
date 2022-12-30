with open("21.txt","w") as f:
    for i in range(10):
        a=i,i**2,i**3
        f.write(str(a))
        f.write("\n")

