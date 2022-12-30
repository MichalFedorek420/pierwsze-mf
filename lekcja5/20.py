import random 
with open("range2.txt", "w") as f:
    for i in range(50):
        f.write(str(random.randint(100,1000)))
        f.write("\n")
