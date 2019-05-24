from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")        #^c stop the program at any minute
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')                             #open the created file , 'w' gave the write access to the file

print("Truncating the file. Goodbye!")
target.truncate()                                        #with the write access it can edit the file created (truncate will delete the file)

print("Now I'm going to ask you for three lines.")

line1=input("line 1: ")
line2=input("line 2: ")
line3=input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()                   #python gave liberty to open the same file again and again and also no need to close the file.