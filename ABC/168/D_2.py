import queue

n, m = map(int, input().split())
table = [[] for i in range(n+1)]
ans = [(1e9, 0) for i in range(n+1)]
seen = [False for _ in range(n+1)]
seen[1] = True

for i in range(m):
    a, b = map(int, input().split())
    # print(table[min(a, b)])
    # table[min(a, b)].append(max(a, b))
    table[a].append(b)
    table[b].append(a)

q = queue.Queue()

q.put((1, table[1]))
while(not q.empty()):
    element = q.get()
    for i in element[1]:
        if seen[i]:
            continue
        ans[i] = element[0]
        seen[i] = True
        q.put((i, table[i]))


if 1e9 in ans[2:]:
    print("No")
else:
    print("Yes")
    for i in ans[2:]:
        print(i)
