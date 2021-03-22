n = int(input())
a_min = (1000000, 1001)
a_min_second = (1000000, 1001)
b_min = (1000000, 1001)
b_min_second = (1000000, 1001)

for i in range(n):
    a, b = map(int, input().split())
    if a_min[0] > a:
        a_min_second = a_min
        a_min = (a, i)
    if b_min[0] > b:
        b_min_second = b_min
        b_min = (b, i)
    # print(a_min, b_min, a_min_second, b_min_second)
if a_min[1] != b_min[1]:
    print(max(a_min[0], b_min[0]))
else:
    print(min(max(a_min[0], b_min_second[0]), max(a_min_second[0], b_min[0]), a_min[0]+b_min[0]))
