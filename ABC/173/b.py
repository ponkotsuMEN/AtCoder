n = int(input())
ans = {"AC":0, "WA":0, "TLE":0, "RE":0}
for i in range(n):
    s = input()
    ans[s] += 1

print("AC x " + str(ans["AC"]))
print("WA x " + str(ans["WA"]))
print("TLE x " + str(ans["TLE"]))
print("RE x " + str(ans["RE"]))
