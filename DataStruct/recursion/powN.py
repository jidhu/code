t=int(input())
for i in range(t):
     n=input()
     v=n[::-1]
     print(v)
     n=int(n)
     v=int(v)
     poww(n,v)
def poww(n,v):
    if v==0:
        return 1

    elif v==1:
        return n
    
    z=(poww(n,v//2))%1000000007
    if v%2==0:
        return((z*z)%1000000007)
    else:
        return((n*((z*z)%1000000007))%1000000007)
    x=poww(n,v)
    print(x)