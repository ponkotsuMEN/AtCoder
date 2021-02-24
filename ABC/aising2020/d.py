def popcount(x):
    return bin(x).count('1')

def f(x):
    if x == 0:
        return 1
    return f(x%popcount(x))+1

n=int(input())
x=input()
xx=int(x,2)
p=x.count('1')
s=xx%(p+1)
if p!=1:
    t=xx%(p-1)
for i in range(n):
    if x[i]=='1':
        if p!=1:
            k=t
            k-=pow(2,n-i-1,p-1)
            k%=p-1
        else:
            print(0)
            continue
    else:
        k=s
        k+=pow(2,n-i-1,p+1)
        k%=p+1
    print(f(k))
