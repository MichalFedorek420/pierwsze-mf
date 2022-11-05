def binary_number(number):
    for e in str(number):
        if e not in ["0","1"]:
            return False


    return True


print("binarny") if binary_number(87655) else print("niebinarny")

print("binarny") if binary_number("0000") else print("niebinarny")
