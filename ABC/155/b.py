n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i%2 == 0:
        if not (i%3==0 or i%5==0):
            print("DENIED")
            print(i)
            exit()
print("APPROVED")
