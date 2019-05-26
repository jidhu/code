#User function Template for python3
def doge_count(str):
    count=0
    str=list(''.join(str))
    try:
        for i in range(0,len(str)):
            if (str[i]=='d')and(str[i+1]=='o')and(str[i+3]=='e'):
                count+=1
                i+=2
    except IndexError:
        return count
    return count

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(doge_count(str))
        testcases-=1

if __name__=='__main__':
    main()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
