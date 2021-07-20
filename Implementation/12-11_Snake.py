import sys
import copy
input = sys.stdin.readline

N = int(input()) # 2 < = N < = 100
apple = int(input())  # 0 < = apple < = 100
count = 0
board = [[0]*(N+2) for _ in range(N+2)]
for i in range(0,N+2):  # 벽은 1
    board[0][i]=1
    board[N+1][i]=1  
    board[i][0]=1
    board[i][N+1]=1
snake_pos = copy.deepcopy(board)

print(board)
current_x,current_y = 1, 1
snake_pos[current_x][current_y] = 3 # snake는 3
looking = 0
tail = 2
dx = [0,1,0,-1] # 동 남 서 북
dy = [1,0,-1,0] # 동 남 서 북

for i in range(apple):
    x, y = map(int,input().split()) # There is no apple on (1,1)
    board[x][y]=2  # apple은 2

L = int(input()) #  1 < = L < = 100
time_list = []
direction_list = []
for i in range(L):
    time, direction = input().split() # There is no apple on (1,1)
    time_list.append(int(time))
    direction_list.append(direction)

snake_length = 1

for t in time_list:
    for direction in direction_list:
        current_x= current_x+dx[looking]
        current_y= current_y+dy[looking]
        snake_pos[current_x][current_y] = 3 # snake는 3
      

        count +=1
        if(snake_posp[current_x][current_y]==1 or snake_posp[current_x][current_y]==3):
            print(count-1)
            break
        elif(board[current_x][current_y]==2):
            if(looking == 3):
                tail = 1 # 남

            elif(looking ==2):
                tail = 0 
            elif(looking==1):
                tail = 3 # 북
                snake_pos[current_x+dx[tail]][current_y+dy[tail]]=3
            elif(looking==0):
                tail = 2
            
    if (direction=="D"):
        if(looking==3):
            looking=0
        else:
            looking+=1
    elif (direction=="L"):
        if(looking==0):
            looking=3
        else:
            looking-=1
    #  dircection L - left / D - right  (90 rotation)
