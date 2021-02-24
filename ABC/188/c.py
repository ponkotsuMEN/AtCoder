n = int(input())
a = list(map(int, input().split()))
all_list = a.copy()

for i in range(n-1):
    player = []
    for j in range(0, 2**(n-i), 2):
        player.append(max(a[j], a[j+1]))
    a = player.copy()

print(all_list.index(min(a)) + 1)
