import math
n, k = map(int, input().split())
a = list(map(int, input().split()))

limit = math.log(n)

if k >= n:
    for i in range(n-1):
        print(n, end=" ")
    print(n)
    exit()

for _ in range(k):
    list = [1]*n
    for i, d in enumerate(a):
        if d == 0:
            continue
        for j in range(-d, d+1):
            if j == 0:
                continue
            if i+j >= 0:
                try:
                    list[i+j] += 1
                    # print(i, j)
                except:
                    pass
    if _ > limit:
        break
    a = list.copy()
for i in range(n-1):
    print(a[i], end=" ")
print(a[-1])
