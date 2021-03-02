n = int(input())
ans = int(pow(10, 9) + 1)
for i in range(n):
    a, p, x = map(int, input().split())
    if x > a:
        ans = min(ans, p)
if ans == int(pow(10, 9) + 1):
    print(-1)
else:
    print(ans)
