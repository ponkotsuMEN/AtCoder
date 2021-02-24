n = int(input())
table = []
sum = 0
count = 0
same = 0
check = [False] * n
for i in range(n):
    a, b = map(int, input().split())
    table.append([a/b, -b/a])

for i in range(n):
    tmp = count
    for j in range(i+1, n):
        if table[i][0] == table[j][1]:
            count += 1
            if check[i]:
                check[i] += 1
            else:
                check[i] = 1
            if check[j]:
                check[j] += 1
            else:
                check[j] = 1
            # sum -= 2**(n-2)
            # print(sum)
for i in range(n):
    if check[i] >= 2:
        sum += 2**(n-3) * (check[i] - 1)
        same += check[i] - 1

sum += 2**n - 1
sum -= 2**(n-2) * count
sum += 2**(n-4) * (count - same)

# print(table)
print(check)
print(same)
print(sum)
# print(count)
