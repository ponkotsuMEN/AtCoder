a, b, c, d = map(int, input().split())
s = a + b + c + d
for i in [a,b,c,d,a+b,a+c,a+d,b+c,b+d,c+d,a+b+c,a+c+d,b+c+d]:
    if i == s - i:
        print("Yes")
        exit()
print("No")
