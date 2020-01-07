n = 8
s = "UDDDUDUU"
level,mountain,valley = 0,0,0

for char in s:
    if char == "U":
        level+=1
    else:
        level-=1
    if level == 0:
        if char == "U":
            valley += 1
        else:
            mountain += 1
            
print(valley)
