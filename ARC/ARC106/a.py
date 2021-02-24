n = int(input())
a = 1
b = 1
while pow(3, a) + pow(5, b) <= n:
    while pow(3, a) + pow(5, b) <= n:
        if pow(3, a) + pow(5, b) == n:
            print(a, b)
            exit()
        b += 1
    b = 1
    a += 1
print(-1)
