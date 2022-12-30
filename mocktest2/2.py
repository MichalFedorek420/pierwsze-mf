def f(human_age):
    if human_age<2:
        human_age=human_age*10
    else:
        human_age=20+(human_age-2)*4
    return(human_age)
print(f(15))