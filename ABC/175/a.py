s = input()
r = s.count('R')
if r == 0:
    print(0)
elif r == 1:
    print(1)
elif r == 3:
    print(3)
else:
    if s[1] == 'R':
        print(2)
    else:
        print(1)
