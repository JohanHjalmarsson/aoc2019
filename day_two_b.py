

def getInput():
    result = []
    f=open("input/day_two")
    for line in f:
        result = map(int, line.split(','))
    return result

def runProgram(list, noun, verb):
    list[1] = noun
    list[2] = verb
    i = 0
    while list[i] != 99: 
        item = int(list[i])
        pos1 = list[i+1]
        pos2 = list[i+2]
        pos3 = list[i+3]
        
        if item == 1:    
            list[pos3] = list[pos1] + list[pos2]
        elif item == 2:
            list[pos3] = list[pos1] * list[pos2]
        i = i+4
    return list


def runProgramWithInput(aim):
    output = 0
    result = 0
    for i in range(100):
        for j in range(100):
            output = runProgram(getInput(), i, j)[0]
            if output == aim:
                result = 100*i+j
                break
        if output == aim:
            break
    return result

print(runProgramWithInput(19690720))
# print(runProgram(getInput(), 12, 2))



