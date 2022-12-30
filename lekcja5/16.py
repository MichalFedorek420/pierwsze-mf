with open("plik420.txt", "r") as f:
    for i in f:
        a=f.readlines()
        print(a)
    with open("plik421.txt","w") as g:
        for i in a:
            g.write(i)