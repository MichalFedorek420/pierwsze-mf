x = 0
y = 0
z = 0
while y!="done":
    try:
        y = input("wpisz liczbe")
        x = x+int(y)
        z = z+1
    except ValueError:
            if y=="done":
                print(x, z, x/z)
            else:
                print("to  nie jest liczba")
