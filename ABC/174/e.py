n, q = map(int, input().split())
c = list(map(int, input().split()))
li = []
dic = {}
for i in range(n):
    try:
        dic[c[i]] += 1
    except:
        dic[c[i]] = 1
    li.append(dic.copy())
# print(li)
for i in range(q):
    l, r = map(int, input().split())
    if l == r:
        print(1)
        continue
    if l == 1:
        print(len(li[r-1]))
        continue
    print(len(li[r-1].items() - li[l-2].items()))
