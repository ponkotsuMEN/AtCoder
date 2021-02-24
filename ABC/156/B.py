n, k = map(int, input().split())
digit = k
num = 1
while n//digit:
    digit *= k
    num += 1
print(num)
