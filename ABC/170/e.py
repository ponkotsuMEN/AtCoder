import time
start = time.time()
n, q = map(int, input().split())
child = []
team = [{} for _ in range(2*pow(10, 5))]
a_max = pow(10, 9)+1
mx = [a_max for _ in range(2*pow(10, 5))]
# print(team)

for i in range(n):
    a, b = map(int, input().split())
    # team[b].append({i: a})
    b -= 1
    team[b][i] = a
    if mx[b] == a_max:
        mx[b] = a
    else:
        mx[b] = max(mx[b], a)
    child.append([a, b])

for i in range(q):
    c, d = map(int, input().split())
    # team[d].append({c: child[c][0]})
    c -= 1
    d -= 1
    a = child[c][0]
    b = child[c][1]
    try:
        mx[d] = max(mx[d], a)
    except:
        mx[d] = a
    team[d][c] = a
    # team[child[c][1]].remove(child[c])
    del team[b][c]
    if mx[b] == a:
        try:
            mx[b] = max(team[b].values())
        except:
            del mx[b]
    child[c] = [a, d]
    # print(team[:8])
    # print(min(mx.values()))
    print(min(mx))

end = time.time()
print(end - start)
