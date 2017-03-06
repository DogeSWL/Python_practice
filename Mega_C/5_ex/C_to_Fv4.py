temperatures=[10,-20,-289,100]

def writeTemp(temp):
    with open("temps.txt", "w") as file:
        for c in temp:
            if c >= -273.15:
                f = ((c*9)/5)+32
                file.write(str(f)+"\n")

writeTemp(temperatures)
