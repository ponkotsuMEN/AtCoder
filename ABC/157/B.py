bingo = []
for i in range(3):
    bingo.append(input().split())

n = int(input())
for i in range(n):
    num = input()
    try:
        for y, row in enumerate(bingo):
            try:
                pos = (y, row.index(num))
                break
            except:
                pass
        bingo[pos[0]][pos[1]] = False
    except:
        pass

for i in range(3):
    if not any(bingo[i]):
        print("Yes")
        exit()
for i in range(3):
    if not (bingo[0][i] or bingo[1][i] or bingo[2][i]):
        print("Yes")
        exit()
if not(bingo[0][0] or bingo[1][1] or bingo[2][2]):
    print("Yes")
    exit()
if not(bingo[0][2] or bingo[1][1] or bingo[2][0]):
    print("Yes")
    exit()
print("No")
