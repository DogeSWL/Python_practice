def change_CF(c):
    if c >= -273.15:
        f = ((c*9)/5)+32
        return f
    else:
        return "Can't go lower than -273.15C"

print(change_CF(-274.15))
