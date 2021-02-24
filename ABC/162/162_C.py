import math
n = int(input())
sum = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        tmp = math.gcd(a, b)
        for c in range(1, n+1):
            sum += math.gcd(tmp, c)
print(sum)
