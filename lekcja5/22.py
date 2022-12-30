import csv
with open("22.csv") as f:
    f_reader=csv.reader(f)
    for i in f_reader:
        if i[2] !="age" and int(i[2]) < 30:
            print(i[0],i[1],i[-1])