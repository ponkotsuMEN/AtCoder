n = int(input())
p = list(map(int, input().split()))
ans = 0
s = set()
for i in p:
    s.add(i)
    while ans in s:
        ans += 1
    print(ans)
