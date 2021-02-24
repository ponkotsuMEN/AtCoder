s = input()
if len(s)%2 == 1 or len(s) == 0:
    print("No")
    exit()
while(len(s)):
    # print(s[:2])
    if s[:2] == "hi":
        if len(s) == 2:
            print("Yes")
            exit()
        s = s[2:]
    else:
        print("No")
        exit()
print("No")
