kasa = int(input("ile zarabiasz"))
godziny = int(input("ile przepracowales"))
if godziny <= 40:
    print(f'zarobiłeś {godziny*kasa}')
else:
    print(f'zarobiłeś {40*kasa+((godziny-40)*kasa*3/2)}') 