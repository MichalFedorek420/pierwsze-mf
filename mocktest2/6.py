import json
def f(age,course,average):
    x=0
    z=0
    avg=0
    licznik=0
    with open("test.json","r") as f:
        d=json.load(f)
        for i in d:
            if i[age] >= age:
                for j in i['studies']['courses']:
                    if j['studies']==course:
                        for k in j['grades']:
                            x=x+k
                            z+=1
                        avg=x//z
                        if avg >=average:
                            licznik+=1
                        else:
                            continue
                    else:
                        continue
            else:
                continue
    return licznik
print(f(21,"statistics",4))