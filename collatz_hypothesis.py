c0 = int(input("Input a number: "))
steps = 0

while c0 != 1:
    if c0 % 2 != 1:
        c0 /= 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    c0 = int(c0)
    print(c0)

print("steps =", steps)