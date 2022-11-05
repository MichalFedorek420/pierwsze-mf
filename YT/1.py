wzrost = int(input("Ile masz wzrostu?"))
wzrost_w_stopach = wzrost*0.0328 #float
wzrost_stopy_int = int(wzrost_w_stopach)
cale = (wzrost_w_stopach-wzrost_stopy_int)*12
print(f"twoj wzrost to {wzrost} cm {wzrost_stopy_int} stóp i {round(cale)}cali")