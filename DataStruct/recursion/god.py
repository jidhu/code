def rec(n,k):
    if n==1:
        return n
    return (rec(n-1,k)+ k - 1 )% n+1
    
n = 5
k = 2
a = rec(n,k)
# a = [lambda n: n for n in range(1,n+2)]
print(a)