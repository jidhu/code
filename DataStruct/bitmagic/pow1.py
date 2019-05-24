T=int(input())
while(T>0):
    N = int(input())
    if N and (not(N&(N-1))):
        print("Yes")
    else:
        print("No")
    T-=1