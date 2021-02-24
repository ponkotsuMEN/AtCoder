x = int(input())
for a in range(-118, 120):
    for b in range(-118, 119):
        if pow(a, 5) - pow(b, 5) == x:
            print(str(a) + " " + str(b))
            exit()
