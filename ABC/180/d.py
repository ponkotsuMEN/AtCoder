x, y, a, b = map(int, input().split())
ans = 0
t = x
while (t*a - t) < b:
    ans += 1
    # t = x * pow(a, ans)
    t *= a
    if t >= y:
        print(ans - 1)
        exit()
ans2, mod = divmod(y - t, b)
if mod == 0:
    ans2 -= 1
print(ans2 + ans)
