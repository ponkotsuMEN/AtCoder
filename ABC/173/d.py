n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
s = 0
s += a[0]
if len(a)%2 == 0:
    s += sum(a[1:len(a)//2]) * 2
else:
    s += sum(a[1:len(a)//2]) * 2 + a[len(a)//2]
print(s)
