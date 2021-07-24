# 어디선가 꼬인 것 같다,,, 시간 안에 못 풀었다.

import sys
input = sys.stdin.readline

def dfs(i,j,graph,visited):
    if i< 0 or i >= N or j < 0 or j >= M :
        return False
    visited[i][j] = 1 # 방문 처리
    # 현재 위치에서 연결된 다른 0 을 재귀적으로 탐색
    for i in range(4):
        i += dx[direction]
        j += dy[direction]
        if i< 0 or i >= N or j < 0 or j >= M :
            i -= dx[direction]
            j -= dy[direction]
            continue
        elif(graph[i][j] == 0):
            if (visited[i][j] == 0):
                dfs(i,j,graph,visited)
                direction +=1
        return True

if __name__ == "__main__":
    N,M = map(int,input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().strip())))

    count = 0 
    visited = [[0]*M for _ in range(N)]
    dx = [-1,0,1,0] # 상 우 하 좌 
    dy = [0,1,0,-1] # 상 우 하 좌

    for i in range(N):
        for j in range(M):
            if dfs(i,j,graph,visited)== True:
                count +=1
    print(count)
    
# 답지를 참고하니, 굳이 visited 그래프를 만들어줄 필요 없고, 빈 공간을 나타내는 0을 방문했으면 그냥 1로 바꿔줌으로써 채워주기만 하면 되었다.
import sys
input = sys.stdin.readline

def dfs(i,j,graph):
    if i< 0 or i >= N or j < 0 or j >= M :
        return False
    # 현재 위치에서 연결된 다른 0 을 재귀적으로 탐색
    if graph[i][j] == 0: 
        graph[i][j] = 1 # 방문 처리
        dfs(i-1,j,graph) # 상
        dfs(i+1,j,graph) # 하 
        dfs(i,j+1,graph) # 좌
        dfs(i,j-1,graph) # 우
        return True
    return False

if __name__ == "__main__":
    N,M = map(int,input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().strip())))

    count = 0 

    for i in range(N):
        for j in range(M):
            if dfs(i,j,graph)== True:
                count +=1
    print(count)
