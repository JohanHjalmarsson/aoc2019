

def getInput():
    result = []
    f=open("input/day_two")
    for line in f:
        result = map(int, line.split(','))
    return result

def runProgram(list):
    list[1] = 12
    list[2] = 2
    i = 0
    while i <= len(list): 
        item = int(list[i])
        pos1 = list[i+1]
        pos2 = list[i+2]
        pos3 = list[i+3]
        if item == 1:    
            list[pos3] = list[pos1] + list[pos2]
            i = i+4
        elif item == 2:
            list[pos3] = list[pos1] * list[pos2]
            i = i+4
        elif item == 99:
            break
        else:
            i = i + 1
    return list

print(runProgram(getInput())[0])



