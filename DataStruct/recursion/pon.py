def reverse(N):
   r = 0
   if (N == 0):
      return 0
   r = r * 10
   r = r + N % 10
   reverse(N/10)
   return r
T = int(input())
while(T>0):
   N = int(input()
   x = 0
   x = reverse(N)
   print(x)
   T-=1