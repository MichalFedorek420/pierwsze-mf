with open("range.txt","w") as f:
    i=None
    for i in range(50):
        i+=1
        f.write(str(i))
        f.write("\n")