temperatures=[10,-20,-289,100]

def change_CF(i):
    if i >= -273.15:
        f = ((i*9)/5)+32
        return float(f)
    else:
        return "That temperature doesn't make sense!"

for i in temperatures:
    print(change_CF(i))
