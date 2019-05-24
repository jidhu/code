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

cipher_text=(list(input("ciphertext: ")))

plain_text=[]
for i in range(0,len(cipher_text)):
    j=ord(cipher_text[i])

    if(j>=65 and j<=90):
        j=j-key
        while(j<65):
            j+=26
        plain_text.append(chr(j))

    elif(j>=97 and j<=122):
        j=j-key
        while(j<97):
            j+=26
        plain_text.append(chr(j))

    else:
        plain_text.append(chr(j))

print('plaintext:',''.join(plain_text))