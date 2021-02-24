import math
n = int(input())
x = list(map(int, input().split()))
ans = [0,0]
tmp = []
for i in range(n):
    ans[0] += abs(x[i])
    ans[1] += abs(x[i])**2
    tmp.append(abs(x[i]))
print(ans[0])
print(math.sqrt(ans[1]))
print(max(tmp))
