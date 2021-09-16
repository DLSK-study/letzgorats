# 맨 처음에 최소 거리로 구성된 그래프부터 만들었는데, i에서 j로가는 비용과 j에서 i로 가는 비용이 다를 수 있었다. 더 최소가 되는 비용을 구하는게 아니라, 아예 양방향이다.
# 다시 풀어서, 플로이드로 접근했다. 플로이드를 접근하고 모든 정점에서 다른 모든 정점으로의 비용이 최소가 되는 그래프를 만들었는데, 거기까지밖에 못 풀었다. 그 이후 구글링,,
# 거기서 나아가 그 그래프를 탐색을 하는 방법으로 dfs나 bfs로 풀면 되는데, 오래돼서 까먹었고 지금 문제점이 재귀적인 로직을 이해하는듯 못하고 있다. 다시 한번, 공부해야 한다. 심각하다ㅠ


# 플로이드 + DFS
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n , start = map(int,input().split())
visited = [False] *(n)
visited[start] = True
answer = int(1e9) 

def dfs(position,visit_count,cost):
    global answer
    
    if visit_count == n:
        answer = min(answer,cost)
        return 
        
    for i in range(n):
        if visited[i] == False: # 아직 방문하지 않았다면,
            visited[i] = True # 방문처리해주고
            dfs(i,visit_count+1,cost+graph[position][i]) # dfs(현재,visit카운트,비용)
            visited[i] = False # 다시 미방문처리

graph = [list(map(int,input().split())) for _ in range(n)]
# i행성에서 j행성까지 가는 최단거리 구하기(플로이드)
# 여기서 이미 방문한 행성도 중복해서 갈 수 있다고 했다.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                graph[i][j]=min(graph[i][k]+graph[k][j],graph[i][j])

# 이제 행성을 탐색하면서 최단 경로를 구하면 된다.

dfs(start,1,0)
print(answer)

# 플로이드 + BFS(힙큐)를 이용하는 방법은 잘안된다,,
