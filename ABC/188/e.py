n, m = map(int, input().split())
a = list(map(int, input().split()))
a_sort = sorted(enumerate(a), key=lambda x: x[1])
# print(a)
# print(a_sort)

town = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    town[x-1].append(y-1)

# print(town)
done = set()
queue = []
ans = [-100000000000] * (n+1)
for mini, _ in a_sort:
    for initial in town[mini-1]:
        if not initial in done:
            queue.append(initial)
            # done.add(initial)
    while len(queue) != 0:
        p = queue.pop(0)
        ans[p] = a[p-1] - a[mini-1]
        for i in town[p]:
            if not i in done:
                queue.append(i)
                done.add(i)
print(max(ans))
