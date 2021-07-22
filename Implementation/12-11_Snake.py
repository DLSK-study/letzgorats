# import sys
# import copy
# input = sys.stdin.readline

# N = int(input()) # 2 < = N < = 100
# apple = int(input())  # 0 < = apple < = 100
# count = 0
# board = [[0]*(N+2) for _ in range(N+2)]
# for i in range(0,N+2):  # 벽은 1
#     board[0][i]=1
#     board[N+1][i]=1  
#     board[i][0]=1
#     board[i][N+1]=1
# snake_pos = copy.deepcopy(board)

# print(board)
# current_x,current_y = 1, 1
# snake_pos[current_x][current_y] = 3 # snake는 3
# looking = 0
# tail = 2
# dx = [0,1,0,-1] # 동 남 서 북
# dy = [1,0,-1,0] # 동 남 서 북

# for i in range(apple):
#     x, y = map(int,input().split()) # There is no apple on (1,1)
#     board[x][y]=2  # apple은 2

# L = int(input()) #  1 < = L < = 100
# time_list = []
# direction_list = []
# for i in range(L):
#     time, direction = input().split() # There is no apple on (1,1)
#     time_list.append(int(time))
#     direction_list.append(direction)

# snake_length = 1

# for t in time_list:
#     for direction in direction_list:
#         current_x= current_x+dx[looking]
#         current_y= current_y+dy[looking]
#         snake_pos[current_x][current_y] = 3 # snake는 3
      

#         count +=1
#         if(snake_posp[current_x][current_y]==1 or snake_posp[current_x][current_y]==3):
#             print(count-1)
#             break
#         elif(board[current_x][current_y]==2):
#             if(looking == 3):
#                 tail = 1 # 남

#             elif(looking ==2):
#                 tail = 0 
#             elif(looking==1):
#                 tail = 3 # 북
#                 snake_pos[current_x+dx[tail]][current_y+dy[tail]]=3
#             elif(looking==0):
#                 tail = 2
            
#     if (direction=="D"):
#         if(looking==3):
#             looking=0
#         else:
#             looking+=1
#     elif (direction=="L"):
#         if(looking==0):
#             looking=3
#         else:
#             looking-=1
#     #  dircection L - left / D - right  (90 rotation)
    

# 그나마 로직이 이해가 갔던 문제인데, 역시 시간안에 못 풀었다.
# 뱀 꼬리부분 제거를 popleft() 로 해결했던 것이 키포인트였다.
# time과 방향커맨드를 딕셔너리로 받은것도 중요했다.
import sys
from collections import deque
input = sys.stdin.readline

def change(d,c):
    # 상 우 하 좌 순
    if c=="L":  # 왼쪽으로 90도 회전
        d = (d-1) % 4 
    else: # "D" : 오른쪽으로 90도 회전
        d = (d+1) % 4
    return d

dy = [-1, 0, 1, 0] # 상 우 하 좌
dx = [0, 1 , 0, -1]  # 상 우 하 좌 

def start():
    direction = 1 # 초기 방향(우)
    time = 1 # 시간
    y,x = 0,0 # 초기 뱀 위치
    visited = deque([[y,x]]) # 방문 위치
    board[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0<=x < N and board[y][x] !=2: 
            if not board[y][x] == 1: # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                board[temp_y][temp_x] = 0 # 꼬리 제거
            
            board[y][x] = 2
            visited.append([y,x])
            if time in times.keys():
                direction = change(direction,times[time])
            time +=1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우라면,
            return time

if __name__ == "__main__":
    N = int(input()) # 2 < = N < = 100
    apple = int(input())  # 0 < = apple < = 100

    board = [[0]*(N) for _ in range(N)]
    for _ in range(0,apple):  # 사과는 1
        a, b = map(int,input().split())
        board[a-1][b-1] = 1   # -1을 하는 이유는 상하좌우 벽 고려해서 -1을 한 것

    L = int(input())
    times = {}
    for i in range(L):
        X,C = input().split()
        times[int(X)]=C
    print(start())
