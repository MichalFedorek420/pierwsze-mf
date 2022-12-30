with open("plik420.txt","r") as f:
    with open("copylines.txt","w") as g:
        for i in f:
            g.write(i)