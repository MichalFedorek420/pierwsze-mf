wzrost = int(input("podaj swoj wzrost:"))

wzrost_w_stopach = wzrost*0.0328 # float
wzrost_w_stopach_int = int(wzrost_w_stopach)
cale = (wzrost_w_stopach - wzrost_w_stopach_int) * 12

print(f"I am {wzrost}cm tall, i.e. {wzrost_w_stopach_int} feet and {round(cale)} inches.")