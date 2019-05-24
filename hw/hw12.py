x=int(input("please enter a number? "))
y=input("enter the same no again ")
print("converted to integer so the output is ",end ='')
print(x*3)
print("Non converted number "+y*3)

age=input("How old are you? ")
height=input("How tall are you? ")
weight=input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print("So, you're {} old, {} tall and {} heavy.".format(age,height,weight))