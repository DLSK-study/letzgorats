# 플로이드 워셜 문제로 풀긴 했으나, m의 범위가 50000이 이기 때문에, m 이 커지면 시간복잡도에서 틀릴 것 같다.
# 다익스트라보다 플로이드가 더 손에 익숙하다,,
# 내가 푼 방법 - 플로이드 워셜 방법
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF] *(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

distance = [[INF] * (n+1)]

for i in range(m):
    a, b= map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if(graph[a][b] != INF or graph[a][b] != 0):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
                
max_val = 0
for j in range(1,n+1):
    if(graph[1][j]!=INF):
        max_val = max(graph[1][j],max_val)

first_index = 1
count = 0
for j in range(1,n+1):
    if(graph[1][j]==max_val):  # 굳이 더 안돌도록 break
        first_index = j
        break

for val in graph[1][first_index:]: # 행 1개만 탐색하면서, count 계산
    if(val==max_val):
        count +=1

print(first_index,max_val,count)

# 다익스트라 최단경로 풀이
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [[] *(n+1) for _ in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):  # 출발, 도착 노드와 해당 비용은 1(양방향)
    a, b= map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    queue = []
    # 초기값은 시작노드 비용= 0
    heapq.heappush(queue,(0,start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

start =1
dijkstra(start)

max_node = 0
max_distance = 0
result = []

for i in range(1,n+1):
    if max_distance < distance[i]:
        max_distance = distance[i]
        max_node = i
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance,len(result))
