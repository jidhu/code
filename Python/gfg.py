T=int(input())
while(T>0):
    N = int(input())
    count=0
    while(N>0):
        if N&1:
            count += 1
        N=N>>1
    print(count)    
    T-=1