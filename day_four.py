low = 172930
high = 683082
amount = 0
while low < high:
    prev = -1
    for x in str(low):
        if int(x) == prev:
            amount = amount + 1
        if int(x) < prev:
            amount = amount - 1
        prev = int(x)
    low = low + 1

print(amount)