h, w = map(int, input().split())
table = []
for i in range(h):
    table.append(input())
ans = 0
for i in range(h):
    for j in range(w-1):
        if table[i][j] == '.' and table[i][j+1] == '.':
            ans += 1

for i in range(h-1):
    for j in range(w):
        if table[i][j] == '.' and table[i+1][j] == '.':
            ans += 1
print(ans)
