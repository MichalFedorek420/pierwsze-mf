def f(amount_to_pay):
    x = amount_to_pay//5
    b = (amount_to_pay-x*5)//2
    c = (amount_to_pay-x*5-b*2)//1
    d = x+b+c
    return d

print(f(343))
