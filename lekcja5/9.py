file = open("zad1.txt", "r")
suma = 0
a=[]
for line in file:
    a.append(int(line.strip("\n")))
for line in range(0,len(a)):
    suma=suma+a[line]

print(f"sum of numbers in file is:", suma)

file.close()
