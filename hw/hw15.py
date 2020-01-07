from sys import argv

script, filename = argv

txt = open(filename)                                        # variable = open(filename)

print ("Here's your file {}: ".format(filename))
print (txt.read())
print ("I'll also ask you to type it again:")
file_again =input("> ")

txt_again = open(file_again)
print(txt_again.read())

print(txt_again.read())
