def f(first_letter,last_letter):
    licznik=0
    with open("test.txt","r") as f:
        for i in f:
            for j in i:
                if j == first_letter or j==last_letter:
                    licznik+=1
    return licznik

print(f("w","r"))