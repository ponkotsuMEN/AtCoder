x, n = map(int, input().split())
if n == 0:
    print(x)
    exit()
p = list(map(int, input().split()))
xp = x
xm = x
for i in range(n+1):
    if not xm in p:
        print(xm)
        exit()
    if not xp in p:
        print(xp)
        exit()
    xp += 1
    xm -= 1
