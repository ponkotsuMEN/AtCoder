n, k = map(int, input().split())
a = list(map(int, input().split()))

if k >= n:
    for i in range(n-1):
        print(n, end=" ")
    print(n)
    exit()

tmp = [1]*n
li = []
for i in range(k):
    li.append(tmp.copy())
for i, d in enumerate(a):
    if d == 0:
        continue
    for j in range(-d, d+1):
        if j == 0:
            continue
        if i+j >= 0:
            try:
                li[0][i+j] += 1
                # print(i, j)
            except:
                pass
for h in range(k):
    print(li[h])
    for i, d in enumerate(li[h]):
        if d == 0:
            continue
        for j in range(-d, d+1):
            if j == 0:
                continue
            if i+j >= 0:
                try:
                    li[h+1][i+j] += 1
                    # print(i, j)
                except:
                    pass

print(li)
for i in range(n-1):
    print(li[-1][i], end=" ")
print(li[-1][-1])
