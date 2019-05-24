def histogram(list):
    for i in list:
        output=''
        while(i > 0):
            output+='@'
            i-=1
        print(output)
histogram([2,4,5,65,67,32])