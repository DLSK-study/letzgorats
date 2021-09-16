# 미로탈출과 비슷한 문제로 생각해서 풀었지만, 최단거리를 잡는 부분에서 또 못풀었다,, 
# 구글링을 했다. 내일 다시 봐야한다. 머리가 아프다...

import sys
from collections import deque
input = sys.stdin.readline

col, row = map(int,input().split())
maze = [list(map(int,input().rstrip())) for _ in range(row)]
# print(maze)
dr = [-1,1,0,0] # 상 하 좌 우
dc = [0,0,-1,1]
# INF = int(1e9)
distance = [[-1] *(col) for _ in range(row)]

queue = deque([])
queue.append((0,0))
distance[0][0] = 0
while queue:
    r,c = queue.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<= nr < row and 0<= nc < col:
            if distance[nr][nc] == -1 :
                if maze[nr][nc] == 0:
                    distance[nr][nc] = distance[r][c]
                    queue.appendleft((nr,nc))
                else:  # 1(벽) 이라면
                    distance[nr][nc] = distance[r][c] + 1                    
                    queue.append((nr,nc))

print(distance[row-1][col-1])
