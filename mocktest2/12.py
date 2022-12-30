def f2(a1,a2):
    licznik=0
    licznik1=0
    for i in a1:
        if len(str(i))==2:
            licznik+=1
    for j in a2:
        if len(str(j))==2:
            licznik1+=1
    if licznik1==licznik:
        return True 
    else:
        return False
print(f2([23,7,16,34],[1,18,79,20,6,111]))