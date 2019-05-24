from sys import argv

try:
    script, key=argv
except:
    print("Oops! You forgot to enter the key")
    exit()
try:
    key==int(key)
    print("Oops! your key should be a word or string")
    exit()
except ValueError:
    pass

key=key.upper()
key=list(key)

for i in range(0,len(key)):
    key[i]=ord(key[i])
    key[i]-=65

plain_text=(list(input("plaintext: ")))
cipher_text=[]
k=0

for i in range(0,len(plain_text)):
    j=ord(plain_text[i])

    if(j>=65 and j<=90):
        j=j+key[k]
        while(j>90):
            j-=26
        cipher_text.append(chr(j))
        k+=1

    elif(j>=97 and j<=122):
        j=j+key[k]
        while(j>122):
            j-=26
        cipher_text.append(chr(j))
        k+=1

    else:
        cipher_text.append(chr(j))

    if(k==len(key)):
        k=0

print('ciphertext:',''.join(cipher_text))