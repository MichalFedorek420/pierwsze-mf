with open("plik420.txt","r") as f:
    count = 0
    a=f.read()
    list = a.split("\n")
    for line in list:
        if line:
            count += 1
    print("calkowita liczba wierszy w pliku tekstowym to:",count)
