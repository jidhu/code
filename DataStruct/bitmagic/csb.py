T = int(input())
while T>0:
    N = int(input())
    bit=0
    while(N>0):
        N = N & (N-1)
        bit+=1
    print(bit)
    T-=1