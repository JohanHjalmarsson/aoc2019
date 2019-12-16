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
    for pos in positions:
        d, s = pos[:1], pos[1:]
        for i in range(0, int(s)):
            if (d == 'R'): lastx += 1
            elif (d == 'L'): lastx -= 1
            elif (d == 'U'): lasty += 1
            elif (d == 'D'): lasty -= 1
            key = str(lastx)+'&'+str(lasty)
            visited[key] = ''
            if key in second:
                s1, s2 = key.split('&')
                vpos = abs(int(s1)) + abs(int(s2))
                if (match == 0):
                    match = vpos
                if (vpos < match):
                    match = vpos
    if (match != 0):
        return match
    return visited

w1 = visitPosition(input[0], {})
w2 = visitPosition(input[1], w1)
print(w2)






