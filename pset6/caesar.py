from sys import argv

try:
    script, key = argv
except ValueError:
    print("Oops! Remember to enter a key with the script")
    exit()

key=int(key)
if(key<=0):
    print("Oops! A key should be a positive number")
    exit()

plain_text=(list(input("plaintext: ")))

cipher_text=[]
for i in range(0,len(plain_text)):
    j=ord(plain_text[i])

    if(j>=65 and j<=90):
        j=j+key
        while(j>90):
            j-=26
        cipher_text.append(chr(j))

    elif(j>=97 and j<=122):
        j=j+key
        while(j>122):
            j-=26
        cipher_text.append(chr(j))

    else:
        cipher_text.append(chr(j))

print('ciphertext:',''.join(cipher_text))