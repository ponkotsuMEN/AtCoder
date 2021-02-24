h, w, t = map(int, input().split())
table = []
for i in range(h):
    c = input()
    table.append(c)

ans = 0
cnt = 0

for i in range(h):
    for j in range(w):
        for k in range(h):
            if k == i:
                continue
            for l in range(w):
                if l == j:
                    continue

                if table[k][l] == '#':
                    cnt += 1
        if cnt == t:
            # print(i, j)
            ans += 1
        cnt = 0
cnt = 0
for tmp in range(h):
    for i in range(h):
        if i == tmp:
            continue
        for j in range(w):
            if table[i][j] == '#':
                cnt += 1
    if cnt == t:
        ans += 1
    cnt = 0

cnt = 0
for tmp in range(w):
    for i in range(h):
        for j in range(w):
            if j == tmp:
                continue
            if table[i][j] == '#':
                cnt += 1
    if cnt == t:
        ans += 1
    cnt = 0

cnt = 0
for i in range(h):
    for j in range(w):
        if table[i][j] == '#':
            cnt += 1
if cnt == t:
    ans += 1
# print(table)
print(ans)
