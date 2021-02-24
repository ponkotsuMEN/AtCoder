h, w = map(int, input().split())
mod = pow(10, 9) + 7
table = [[0]*w for _ in range(h)]
table[0][0] = 1
m = []
for i in range(h):
    m.append(input())
# print(table)
# print(m)
for j in range(w):
    for i in range(h):
        if m[i][j] == '#':
            continue
        tmp_i = i-1
        tmp_j = j-1
        i_flag = False
        j_flag = False
        ij_flag = False
        while not (i_flag and j_flag and ij_flag):
            if not i_flag:
                if m[tmp_i][j] == '#' or tmp_i < 0:
                    i_flag = True
                else:
                    table[i][j] += table[tmp_i][j]
                    table[i][j] %= mod
            if not j_flag:
                if m[i][tmp_j] == '#' or tmp_j < 0:
                    j_flag = True
                else:
                    table[i][j] += table[i][tmp_j]
                    table[i][j] %= mod
            if not ij_flag:
                if m[tmp_i][tmp_j] == '#' or tmp_i < 0 or tmp_j < 0:
                    ij_flag = True
                else:
                    table[i][j] += table[tmp_i][tmp_j]
                    table[i][j] %= mod
            tmp_i -= 1
            tmp_j -= 1

print(table[-1][-1])
