n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if (b - a) % 2 == 0:
        ans += (a + b) * ((b - a) // 2) + (b + a) // 2
    else:
        ans += (a + b) * ((b - a + 1) // 2)
print(ans)
