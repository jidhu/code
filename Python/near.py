#User function Template for python3
def isNeighbor(num):
    ##Your code here
    num = num % 10
    if (num<=2)or(num>=8):
        return True
    else:
        return False

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n=int(input())
        print(isNeighbor(n))
        testcases-=1

if __name__=='__main__':
    main()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
