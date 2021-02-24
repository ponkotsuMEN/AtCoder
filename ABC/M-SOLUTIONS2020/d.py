n = int(input())
a = list(map(int, input().split()))
cash = 1000
bill = 0
table = []

for i in range(n-1):
    if a[i] > a[i+1]:
        table.append(False)
    elif a[i] == a[i+1]:
        table.append("-")
    else:
        table.append(True)
# print(table)
if table[0] == True:
    bill, cash = divmod(cash, a[0])
# print(cash, bill)
i = 0
while i < n-1:
    if table[i] == True:
        while not table[i] == False:
            i += 1
            if i == n-1:
                break
        cash += bill * a[i]
        bill = 0
        # print(cash, bill)
    else:
        while not table[i] == True:
            i += 1
            if i == n-1:
                break
        bill, cash = divmod(cash, a[i])
        # print(cash, bill)
cash += bill * a[-1]
print(cash)
