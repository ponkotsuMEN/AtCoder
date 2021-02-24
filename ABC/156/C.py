n = int(input())
x = list(map(int, input().split()))
ave = sum(x)//n
ans1 = 0
ans2 = 0
for i in x:
    ans1 += (i-ave)**2
    ans2 += (i-ave-1)**2
print(min(ans1, ans2))
