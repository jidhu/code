top=10
x=f"There are {top} types of people."

binary="binary"
do_not='don\'t'
y=f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious=False

joke_eval="Isn't that joke so funny?! {}"

print(joke_eval.format(hilarious))

w="This is the left side of ..."
e="a string with a right side."

print(w+e)
print(w,e)