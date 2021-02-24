n = int(input())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (table[k][0] - table[j][0]) * (table[j][1] - table[i][1]) == (table[j][0] - table[i][0]) * (table[k][1] - table[j][1]):
                print("Yes")
                exit()
print("No")
