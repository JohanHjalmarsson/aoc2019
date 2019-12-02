import math

def calMass(mass):
    fuel = int(int(mass)/3)-2
    total = 0
    while fuel > 0:
        total = total + fuel
        fuel = int(int(fuel)/3)-2
    return total

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