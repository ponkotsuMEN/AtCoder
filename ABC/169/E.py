n = int(input())
a = []
b = []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
a.sort()
b.sort()
if n%2 == 0:
    print(b[n//2] + b[n//2-1] - a[n//2] - a[n//2-1] + 1)
else:
    print(b[n//2] - a[n//2] + 1)
