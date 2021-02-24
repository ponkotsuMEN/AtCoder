n, x, t = map(int, input().split())
ans = 0
while(n > 0):
    n -= x
    ans += t
print(ans)
