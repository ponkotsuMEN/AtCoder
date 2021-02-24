n, k = map(int, input().split())
people = [False for i in range(n)]
for i in range(k):
    input()
    a = map(int, input().split())
    for j in a:
        people[j-1] = True
print(people.count(False))
