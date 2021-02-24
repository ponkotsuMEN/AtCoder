n = int(input())
table = [[0, 0] for _ in range(n+1)]
table[0] = [1, 1]
for i in range(n):
    s = input()
    if s == "AND":
        table[i+1][0] += table[i][0]
        table[i+1][1] += table[i][0] + table[i][1]*2
    if s == "OR":
        table[i+1][0] += table[i][0]*2 + table[i][1]
        table[i+1][1] += table[i][1]
print(table[n][0])
