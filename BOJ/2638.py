import sys
from collections import deque
input = sys.stdin.readline

dr = [-1,1,0,0] # 상 하 좌 우 
dc = [0,0,-1,1]
n,m = map(int,input().split())
visited = [[False]*m for _ in range(n)]
graph = [list(map(int,input().split())) for _ in range(n)]
answer = 0

# 바깥 공기를 -1로 초기화
def outSide():
    dq = deque()
    out_visited = [[False]*m for _ in range(n)]
    dq.append((0,0))
    out_visited[0][0] = True
    graph[0][0] = -1 
    while dq:
        r,c = dq.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 > nr or nr >=n or 0 > nc or nc >= m:
                continue
            if graph[nr][nc] == 1 or out_visited[nr][nc] :
                continue
            dq.append((nr,nc))
            graph[nr][nc] = -1
            out_visited[nr][nc] = True
    return 

# 치즈가 다 녹았는지 확인
def isMelt():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                return False
    return True

while not isMelt(): # 치즈가 다 녹을 때 까지 반복
    outSide()   # 바깥 공기를 -1 로 초기화
    check = []  # 바깥 공기와 맞닿은 칸을 저장
    # 외부 공기와 접촉한 치즈는 녹는다.
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt = 0 # 바깥 공기와 맞닿은 칸의 개수
                for k in range(4):
                    nr = dr[k] + i
                    nc = dc[k] + j
                    if 0 > nr or nr >=n or 0 > nc or nc >= m:
                        continue
                    if graph[nr][nc] == -1 :
                        cnt += 1
                if cnt >= 2 : # 2칸 이상 맞닿아야지 녹을 수 있다.
                    check.append([i,j])
    for r,c in check:  # 바깥 공기와 맞닿은 칸은 녹음
        graph[r][c] = 0
    answer += 1

print(answer)
