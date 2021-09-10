# dfs 로 풀긴 했다. ( 이렇게 영역을 구하는 문제는 dfs,bfs 문제 다 사용 가능하다.)
#  맨 처음에는 음료수 얼려먹기 처럼 풀었는데, 1과 0으로만 이루어진 것이 아니어서 어디선가 꼬였다.
# 계속 풀다가 시간이 오래 걸려서 구글링을 살짝 했다.

import sys
sys.setrecursionlimit(100000)  # DFS 를 써야하므로 처음 세팅은 이렇게 해주면 좋다
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
max_rainfall = max(map(max,board))   # map을 이용한 2차원 배열에서 최대 원소 찾기
dr = [-1,1,0,0] # 상 하 좌 우 
dc = [0,0,-1,1]

def dfs(r,c,rainfall):
    for d in range(4):  # 상 하 좌 우 방향으로 탐색하면서 
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc] and board[nr][nc] > rainfall :  # 인덱스 범위가 들어오고 아직 방문하지 않고 해당 강수량보다 크면
            visit[nr][nc] = True   # 방문 처리 하고
            dfs(nr,nc,rainfall)    # 또 dfs 한다.


answer = 1
for k in range(max_rainfall):    #  max_rainfall 바로 전까지 for문을 돌면서 
    visit = [[False]*(n) for _ in range(n)]
    cnt = 0  # cnt 를 초기값 0으로 잡고
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and not visit[i][j]:  # 해당 원소 값이 지금 돌고 있는 강수량보다 크고 아직 방문하지 않은 곳이라면
                visit[i][j] = True  # 방문처리를 해주고
                dfs(i,j,k)   # dfs 한다.
                cnt+=1    # cnt 1 증가 시켜주고
    answer = max(cnt,answer)   # cnt 와 현재 answer를 비교해서 더 큰 값을 answer로 할당

print(answer)   # for문 다 돌면 최종 answer의 값을 출력


# BFS 로 푸는 방법 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
max_rainfall = max(map(max,board))
dr = [-1,1,0,0] # 상 하 좌 우 
dc = [0,0,-1,1]

def bfs(r,c,rainfall,visit):
    queue = deque()
    queue.append((r,c))
    visit[r][c] = True
    while queue:
        r , c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n :
                if visit[nr][nc] == False and board[nr][nc] > rainfall :
                    visit[nr][nc] = True
                    queue.append((nr,nc))


answer = 1
for k in range(max_rainfall):
    visit = [[False]*(n) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and visit[i][j] == False:
                bfs(i,j,k,visit)
                cnt+=1
    answer = max(cnt,answer)

print(answer)
