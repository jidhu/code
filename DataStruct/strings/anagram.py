s1 = 'asdfg'
s2 = 'gadsdfa'
s1 = [char for char in s1]
s2 = [char for char in s2]

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = [0]*256
    for i in range(0,len(s1)):
        count[i]=count[i]+1

    for i in range(0,len(s2)):
        count[i]-=1

    for i in range(256):
        if count[i] != 0:
            return False

    return True

print(anagram(s1,s2))