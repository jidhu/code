def histogram(list):
    for i in list:
        output=''
        while(i > 0):
            output+='*'
            i-=1
        print(output)
histogram([i for i in range(1,9)])
