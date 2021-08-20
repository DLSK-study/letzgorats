# 개념정리 부분에서 구현한 다익스트라 최단 경로 알고리즘의 틀(?)이 계속 반복되는
# 문제들이다. 이게 내가 직접 푼 것보단 단기기억으로 푸는것 같다..bfs로도 풀려고 했으나, 마지막 좌표값이 적절한 최단경로로 나오지 않을 수 있다.
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
test = int(input())
for _ in range(test):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))

    dr = [-1,1,0,0] # 상 하 좌 우
    dc = [0,0,-1,1]
    r = 0 
    c = 0
    distance = [[INF] *(n) for _ in range(n)]
    queue = [(graph[0][0],0,0)] # bfs 로 풀면 그리디 처럼, 그 순간의 최선의 값이 선택된다. 최단경로 알고리즘으로 풀어야 한다.
    distance[r][c] = graph[0][0]
    while queue:
        cost, r,c = heapq.heappop(queue)
        if distance[r][c] < cost: # 이미 처리 되었다면, 계속 진행
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >=n or nc < 0 or nc >= n:
                continue
            weight = cost + graph[nr][nc]
            if weight < distance[nr][nc]: # 현재 노드를 거쳐서 가는 경우가 더 비용이 짧은 경우
                distance[nr][nc] = weight
                heapq.heappush(queue,(weight,nr,nc))

    print(distance[n-1][n-1])
