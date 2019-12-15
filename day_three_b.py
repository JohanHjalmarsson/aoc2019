def getInput():
    result = []
    f=open("input/day_three")
    for line in f:
        result.append(line.rstrip().split(','))
    return result

input = getInput()

def visitPosition(positions, second):
    visited = {}
    match = 0
    lastx, lasty = 0,0
    steps = 0
    lowestSteps = 0
    for pos in positions:
        d, s = pos[:1], pos[1:]
        for i in range(0, int(s)):
            if (d == 'R'): lastx += 1
            elif (d == 'L'): lastx -= 1
            elif (d == 'U'): lasty += 1
            elif (d == 'D'): lasty -= 1
            key = str(lastx)+'&'+str(lasty)
            steps += 1
            visited[key] = steps 
            if key in second:
                s1, s2 = key.split('&')
                intersection = second[key] + steps
                if (lowestSteps == 0):
                    lowestSteps = intersection
                if (intersection < lowestSteps):
                    lowestSteps = intersection
    if (lowestSteps != 0):
        return lowestSteps
    return visited

w1 = visitPosition(input[0], {})
w2 = visitPosition(input[1], w1)
print(w2)






