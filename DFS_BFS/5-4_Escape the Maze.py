# 시간안에 못 풀었다. 가장 가까운 노드부터 탐색하기 때문에 BFS로 풀어야 하고, 
# (n-1,m-1) 까지 가야 탈출하므로, count 라는 전역 변수를 설정해서 푸는 것 보다, 갈 수 있는 길의 값이 1이고 
# 가장 오른쪽 아래 위치로 이동하는 것을 요구하는것에 맞춘다면, 특정 노드를 방문하면, 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는 것이 특징이다.
# 최단 경로 유형도 풀어봐야 할 것 같다.

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().strip())))

# visited = [[0]*M for _ in range(N)]
dx = [-1,1,0,0] # 상 하 좌 우
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    # count = 1
    while queue:
        x,y = queue.popleft()
        for d in range(4): 
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue # 범위 벗어나면 무시
            if graph[nx][ny] == 0 : # 괴물 부분 무시
                continue
            if graph[nx][ny] == 1 : # 갈 수 있으면
                graph[nx][ny] = graph[x][y] + 1 # 해당 노드를 이제 처음 방문한 것일 때만 최단 거리 기록
                queue.append((nx,ny)) 
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N-1][M-1]

print(bfs(0,0))
