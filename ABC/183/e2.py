h, w = map(int, input().split())
mod = pow(10, 9) + 7
table = [[0]*w for _ in range(h)]
table[0][0] = 1
m = []
for i in range(h):
    m.append(input())
# print(table)
# print(m)
it = [[0]*w for _ in range(h)]
jt = [[0]*w for _ in range(h)]
ijt = [[0]*w for _ in range(h)]
for j in range(w):
    for i in range(h):
        if m[i][j] == '#':
            
            continue

        table[i][j] += it[i-1][j] * 2
        table[i][j] %= mod
        it[i][j] = it[i-1][j] * 2
        tmp_j = j-1
        while tmp_j >= 0:
            if m[i][tmp_j] == '#':
                break
            table[i][j] += table[i][tmp_j]
            table[i][j] %= mod
            tmp_j -= 1
        tmp_i = i-1
        tmp_j = j-1
        while tmp_i >= 0 and tmp_j >= 0:
            if m[tmp_i][tmp_j] == '#':
                break
            table[i][j] += table[tmp_i][tmp_j]
            table[i][j] %= mod
            tmp_i -= 1
            tmp_j -= 1
        # print(table)
print(table[-1][-1])
