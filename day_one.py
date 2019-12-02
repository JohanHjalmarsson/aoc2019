import math

def calMass(mass):
    return int(int(mass)/3)-2

def getInput():
    with open("input/day_one") as f:
        c = f.readlines()
    c = [x.rstrip() for x in c] 
    return c

def calInput():
    sum = 0
    for i in getInput():
        sum = sum + calMass(i)
    return sum

print(calInput())