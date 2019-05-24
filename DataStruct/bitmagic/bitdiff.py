T=int(input())
while(T>0):
    a,b =map(int,input().split())
    bit = 0
    a = a^b
    while(a>0):
        a = a&(a-1)
        bit+=1
    print(bit)
    T-=1