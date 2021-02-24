n, k = map(int, input().split())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))

ans = 0
def dfs(end, next, cost):
    global ans
    cost += table[end[-1]][next]
    end.append(next)
    if len(end) == n:
        dfs(end.copy(), 0, cost)
        return
    if len(end) == n+1:
        if cost == k:
            ans += 1
            return
    if cost >= k:
        return
    for i in range(n):
        if not i in end:
            dfs(end.copy(), i, cost)

end = [0]
next = []

for i in range(1, n):
    dfs(end.copy(), i, 0)
print(ans)
