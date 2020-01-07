#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3, arg4, arg5, arg6, arg7 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes one arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw", "who", ' the', ' hell', ' are', ' you?')
print_two_again("Ji","dhu")
print_one("first!")
print_none()
