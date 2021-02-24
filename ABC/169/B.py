import numpy
n = int(input())
a = list(map(int, input().split()))
ans = 1
a.sort()
if a[0] == 0:
    print(0)
    exit()
# ans = numpy.prod(a)
for i in range(n):
    ans *= a[i]
    if ans > pow(10, 18):
        print(-1)
        exit()
else:
    print(ans)
