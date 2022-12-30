def f(dictionary,grade):
    x=[]
    for i in dictionary['subject']['grades']:
        x.append(i)
    if grade in x:
        return True
    else:
        return False
    

print(f({"subject":{"name":"math","grades":[6,3,4]}},3))