import math
n = int(input())
# ans = [0 for _ in range(n)]
ans = [0] * n

for x in range(1, int(math.sqrt(n+1))):
    x2 = x*x
    for y in range(1, int(math.sqrt(n+1))):
        y2 = y*y
        xy = x * y
        tmp = x2 + y2 + xy
        if tmp >= n:
            break
        for z in range(1, int(math.sqrt(n+1))):
            tmp2 = tmp + z*z + y*z + z*x
            if tmp2 > n:
                break
            try:
                ans[tmp2 - 1] += 1
                # print(x, y, z)
            except:
                pass
for i in range(n):
    print(ans[i])
