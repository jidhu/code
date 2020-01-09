arr =[[-9, -9, -9, 1, 1, 1],
      [0, -9, 0, 4, 3, 2],
      [-9, -9, -9, 1, 2, 3],
      [0, 0, 8, 6, 6, 0],
      [0, 0, 0, -2, 0, 0],
      [0, 0, 1, 2, 4, 0]]

ans=[]
row,column,sum=0,0,0
for i in range(4):
    for j in range(4):
        for row in range(i,i+3):
            for column in range(j,j+3):
                if row == i+1:
                    if column==j+1:
                        sum += arr[row][column]
                else:
                    sum += arr[row][column]
        ans.append(sum)
        sum=0
print(max(ans))
