# 풀다가 시간초과, 아직 dx,dy를 활용한 방법이 손에 안 잡힌다.
# 익숙한 유형이므로 익히자
'''숙지해야 할 개념
# global 변수에 대한 활용 + visit 리스트와 원래 map 리스트를 둘 다 확인 해야 하는 점
# x + dx[directoin] 와 y + dy[direction] : 나아 가는 것
# x - dx[directoin] 와 y - dy[direction] : 뒤로 가는 것
# dx와 dy의 direction의 인덱스는 같이 움직인다.'''

import sys
input = sys.stdin.readline

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

N, M = map(int, input().split())
x, y, d = map(int, input().split())
dx = [-1, 0, 1, 0]  # x 이동 ( 북 동 남 서 )
dy = [0, 1, 0, -1]  # y 이동 ( 북 동 남 서 )
visit_map = [[0]*M for _ in range(N)]  # 일단 처음에는 다 방문 안함

visit_map[x][y] = 1  # 현재 위치 방문처리

# 전체 맵
board = []
# board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    # 0 은 육지, 1 은 바다 # 외곽은 항상 바다 1
    board.append(list((map(int, input().split()))))

room = 1
turn_time = 0
while True:
    turn_left()
    current_x = x + dx[d]
    current_y = y + dy[d]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if(visit_map[current_x][current_y] == 0 and board[current_x][current_y] == 0):
        visit_map[current_x][current_y] = 1
        x = current_x
        y = current_y
        room += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 이미 방문했거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 가봤거나 갈 수 없는 경우
    if turn_time == 4:
        current_x = x - dx[d]
        current_y = y - dy[d]
        # 뒤로 이동할 수 있다면 이동
        if board[current_x][current_y] == 0:
            x = current_x
            y = current_y
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(room)
