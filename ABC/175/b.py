n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if l[i] == l[j]:
            continue
        s = l[i] + l[j]
        for k in range(j+1, n):
            if l[i] == l[k] or l[j] == l[k]:
                continue
            if s > l[k]:
                ans += 1
print(ans)
