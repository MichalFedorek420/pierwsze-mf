def f():
    global arr
    global arr1
    arr = ["water","pop","sky"]
    arr1 = ["water","wood","sky"]
    if arr == arr1:
        return str("jest_git")
    else:
        return str("nie jest git")
print(f())
print(arr)
print(arr1)


