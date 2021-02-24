n, m = map(int, input().split())
condition = []
for i in range(m):
    a, b = map(int, input().split())
    condition.append([a, b])
k = int(input())
choose = []
for i in range(k):
    c, d = map(int, input().split())
    choose.append([c, d])

ans = 0
for bit in range(2**k):
    state = [0] * (n+1)
    for shift in range(k):
        plate = choose[shift][bit >> shift & 1]
        # print(plate)
        state[plate] += 1
    num = 0
    for cond in condition:
        # print(cond)
        if state[cond[0]] > 0 and state[cond[1]] > 0:
            num += 1
    ans = max(ans, num)
print(ans)
