n = int(input())
town = []
for i in range(n):
    town.append(list(map(int, input().split())))
print(town)

ans = 0
end = set()
end.add(0)
def distance(now):
    dis = 1000000007
    loc = 0
    for i in range(1, n):
        if i in end:
            continue
        tmp_dis = abs(town[i][0] - town[now][0]) + abs(town[i][1] - town[now][1]) + max(0, town[i][2] - town[now][2])
        if tmp_dis < dis:
            dis = tmp_dis
            loc = i
    end.add(loc)
    return (dis, loc)
next = 0
while not len(end) == n:
    tmp = distance(next)
    print(tmp)
    ans += tmp[0]
    next = tmp[1]
tmp = abs(town[next][0] - town[0][0]) + abs(town[next][1] - town[0][1]) + max(0, town[0][2] - town[next][2])
print(tmp, next)
ans += tmp
print(ans)
