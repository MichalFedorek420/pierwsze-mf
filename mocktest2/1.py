def f(player1,player2):
    sum1=0
    sum2=0
    for i in player1:
        if i=="A" or i=="K" or i=="Q" or i=="J" or i=="T":
            sum1+=10
        else:
            sum1+=int(i)
    for i in player2:
        if i=="A" or i=="K" or i=="Q" or i=="J" or i=="T":
            sum2+=10
        else:
            sum2+=int(i)
    print(sum1,sum2)
    if sum1>sum2:
        return("Wygrywa gracz 1")
    else:
        return("Wygrywa gracz 2")
print(f("AJ972","AQT72"))
    