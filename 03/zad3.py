try: 
    ocena = input("podaj ocene od 0.1 do 1.0: ")
    ocena = float(ocena)
    if ocena > 0 and ocena <= 1:
        if ocena < 0.6:
            print("f")
        elif ocena >= 0.6 and ocena < 0.7:
            print("d")
        elif ocena >= 0.7 and ocena < 0.8:
            print("c")
        elif ocena >= 0.8 and ocena < 0.9:
            print("b")
        elif ocena >= 0.9:
            print("a")
    elif ocena < 0 or ocena > 1:
        print("please enter a number between 0 and 1")
except ValueError: 
    print("please enter float value")