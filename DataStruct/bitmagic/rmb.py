T = int(input())
while T>0:
    m,n = map(int,input().split(' '))
    if m==n:
        print(-1)
    else:
        m=m^n
        for i in range(1,32):
            if m&(1<<(i-1))!=0:
                print(i)
                break
    T-=1