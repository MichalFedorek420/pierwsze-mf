pin = "0805"
x = ""
y = 0
while y<3:
    x = input("podaj pin")
    y += 1
    if x == pin:
        print("wszystko git")
        break
    else:
        print("zly pin")
    if y == 3:
        print("karta zablokowana")