# 내가 푼 방법

import sys
input = sys.stdin.readline

N = int(input())
plan = list(input().split())
current_X = 0  # 현재 x 위치 (열)
current_Y = 0  # 현재 y 위치 (행) 
for cmd in plan:
    if(cmd == 'L'):   # L 일 때는 ( left)
        if(current_X == 0):   # 열 위치가 0번째인지만 확인하면 된다
            continue
        else:
            current_X -= 1
    elif(cmd == 'R'):  #  R일 때는 (right)
        if(current_X == N-1):   # 열 위치가 N-1 번째인지만 확인하면 된다.
            continue
        else:
            current_X += 1
    elif(cmd == 'D'):   # D일 때는 (down)
        if(current_Y == N-1):    # 행 위치가 N-1 번째인지만 확인하면 된다.
            continue
        else:
            current_Y += 1
    elif(cmd == 'U'):    #  U 일때는  (up)
        if(current_Y == 0):   # 행 위치가 0번째인지만 확인하면 된다.
            continue
        else:
            current_Y -= 1
            
print(current_Y+1, current_X+1)
