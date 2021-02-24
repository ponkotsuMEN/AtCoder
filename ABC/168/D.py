
n, m = map(int, input().split())
table = [[] for i in range(n+1)]
ans = [(1e9, 0) for i in range(n+1)]
seen = [False for _ in range(n+1)]
seen[1] = True
def func(node, num, li):
    tmp = []
    print(li)
    for i in li:
        if seen[i]:
            continue
        seen[i] = True
        tmp.append(i)
        # if num < n:
        #     if num < ans[i][0]:
        #         ans[i] = (num, node)
        #         func(i, num+1, table[i])
        ans[i] = (num, node)
    print(ans)
    for i in tmp:
        func(i, num+1, table[i])
            # print(ans[2:])



# print(table)
for i in range(m):
    a, b = map(int, input().split())
    # print(table[min(a, b)])
    # table[min(a, b)].append(max(a, b))
    table[a].append(b)
    table[b].append(a)

# print(table)


num = 1



func(1, num, table[1])
# print(ans[2:])
ans_ = []
for i in ans[2:]:
    ans_.append(i[1])
# print(ans_)
if 1e9 in ans_:
    print("No")
else:
    print("Yes")
    for i in ans_:
        print(i)


# print(table)
