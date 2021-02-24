n = int(input())
dic = {}
for i in range(n):
    s = input()
    try:
        dic[s] += 1
    except:
        dic[s] = 1

mx = max(dic.values())
sorted = sorted(dic.items())

ans = []
for i in sorted:
    if i[1] == mx:
        print(i[0])
