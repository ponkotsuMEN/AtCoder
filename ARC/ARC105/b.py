n = int(input())
a = list(map(int, input().split()))
import math

if n == 1:
    print(a[0])
    exit()

ans = math.gcd(a[0], a[1])
for i in range(2, n):
    ans = math.gcd(ans, a[i])
print(ans)
