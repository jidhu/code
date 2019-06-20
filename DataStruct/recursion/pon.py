T = int(input())
while(T>0):
    N = int(input())
    
    long reverse(long n) {
   static long r = 0;
   
   if (n == 0)
      return 0;
   
   r = r * 10;
   r = r + n % 10;
   reverse(n/10);
   return r;
}
    
    T-=1