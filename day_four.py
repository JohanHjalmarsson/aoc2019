low = 172930 
high = 683082
amount = 0
while low < high:
    prev = -1
    add = False
    for x in str(low):
        if int(x) == prev:
            add = True
        if int(x) < prev:
            add = False
            break
        prev = int(x)
    amount = add and amount + 1 or amount
    low = low + 1
print(amount)