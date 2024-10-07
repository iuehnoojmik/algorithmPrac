position = input()
count = 0

x = int(ord(position[0]) - 96)
y = int(position[1])

moveX = [2,2,-2,-2,1,-1,1,-1]
moveY = [1,-1,1,-1,2,2,-2,-2]

for i in range(8):
    newX = x + moveX[i]
    newY = y + moveY[i]
    
    if newX<1 or newX>8 or newY<1 or newY>8:
        continue
    else:
        count += 1

print(count)
