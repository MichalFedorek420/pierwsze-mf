def card_number(ada):
    ada = str(ada)
    x = None
    if len(ada) == 16:
        x = (ada[0:2] +"**********"+ada[10:15])
    else:
        x = "złe hasło"
    return x

print(card_number(1234567890123456))
