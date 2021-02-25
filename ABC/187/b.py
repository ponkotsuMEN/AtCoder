n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

ans = 0
for left in range(n):
    for right in range(left+1, n):
        if (points[right][0] - points[left][0]) == 0:
            continue
        if -1 <= (points[right][1] - points[left][1]) / (points[right][0] - points[left][0])  <= 1:
            ans += 1
print(ans)
