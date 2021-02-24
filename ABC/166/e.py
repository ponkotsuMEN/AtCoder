n = int(input())
a = list(map(int, input().split()))
sum = 0
l_list = []
r_list = []
for i, a_ in enumerate(a):
    l_list.append(i + a[i])
    r_list.append(i - a[i])

for i, left in enumerate(l_list):
    sum += r_list[i:].count(left)

print(sum)
