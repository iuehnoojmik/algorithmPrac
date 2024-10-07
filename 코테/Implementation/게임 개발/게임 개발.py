n, m = map(int, input().split())
a, b, idx = map(int, input().split())
direction = [0,1,2,3] #북/동/남/서
move = [(0,-1),(1,0),(0,1),(-1,0)] #북/동/남/서
gameMap = []
result = 0
returnFlag = False

for i in range(n):
    gameMap.append(list(map(int,input().split())))


while(returnFlag == False):
    # 현재 위치 1로 변경
    gameMap[a][b] = 1

    # 방향 탐색
    for i in range(-1,3,1):
        newA = a + move[(idx+i)%4][0]
        newB = b + move[(idx+i)%4][1]
        
        if gameMap[newA][newB] == 0: # 방문하지 않은 칸이 있을 경우
            idx = direction[idx+i]
            a = newA
            b = newB
            result += 1
        else: # 모두 방문했던 칸일 경우
            newA = a + move[(idx+2)%4][0]
            newB = b + move[(idx+2)%4][1]
            if gameMap[newA][newB] == 0: # 뒷 칸을 방문하지 않았을 경우
                a = newA
                b = newB
                result += 1
            else:
                returnFlag = True


print(result)
