def f(number, even):
    result = []
    for e in str(number):
        if int(e) % 2 == 0:
            if even == True:
                result.append(int(e))
        else:
            if even == False:
                result.append(int(e))

    return sum(result)

print(f(3242, True))
