n, m, x = map(int, input().split())

c = []
ans = pow(10, 9)

for i in range(n):
    c.append(list(map(int, input().split())))
for mask in range((1 << n) - 1):
    sum = 0
    li = [0] * m
    for i in range(n):
        if (mask >> i) & 1 == 0:
            sum += c[i][0]
            for j in range(m):
                li[j] += c[i][j+1]
    check = True
    for j in range(m):
        if li[j] < x:
            check = False
            break
    if check:
        ans = min(sum, ans)

if ans == pow(10, 9):
    print(-1)
else:
    print(ans)
