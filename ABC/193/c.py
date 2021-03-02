n = int(input())
sqrt = int(n ** 0.5)
s = set()
for a in range(2, sqrt+1):
    b = 2
    while pow(a, b) <= n:
        s.add(int(pow(a, b)))
        b += 1
print(n - len(s))
