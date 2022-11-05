def card_number():
    ada = input("podaj numer konta bankowego: ")
    if len(ada) == 16:
        print (ada[0:2],"**********",ada[10:15])
    else:
        print("złe hasło")

card_number()
