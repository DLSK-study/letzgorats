# 비용이 따로 존재하는 최단 경로 문제로 다익스트라 최단경로 알고리즘을 heapq로 푸는 문제이다.
# 공부하는 차원에서 풀었다.

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, edge, c = map(int,input().split())
graph = [[] for _ in range(n+1)] # 각 노드에 연결되어 있는 "노드"에 대한 정보가 담긴 리스트
distance = [INF] *(n+1) # 최단 거리를 우선 모두 무한으로 초기화
for i in range(edge):
    x,y,cost = map(int,input().split())
    graph[x].append((y,cost))  # x에서 y로 가는 노드와, 비용 저장

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하고 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 빌 때 까지 반복
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 기존의 distance의 최단거리 값이 꺼낸 거리값보다 작으면 무시
            continue
        # 현재 노드와 연결된 다른 노드들을 확인
        for i in graph[now]:
            weight = dist + i[1] # 다른 노드까지의 비용과 현재 꺼낸 거리값을 더해보고
            if weight < distance[i[0]]:  # 현재까지 그 노드까지의 최단거리보다 작으면
                distance[i[0]] = weight # 갱신
                heapq.heappush(q,(weight,i[0])) # 그리고 큐에 넣는다.

dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d!=INF:
        count+=1
        max_distance = max(max_distance,d)

# 시작 노드는 제외해야 하므로 count-1을 출력
print(count-1,max_distance)
