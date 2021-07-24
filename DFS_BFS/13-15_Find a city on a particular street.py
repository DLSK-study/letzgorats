# 역시 시간안에 못 풀었고, 처음에 풀었던 아래 코드는
# 테스트 케이스에 국한되어서 풀었던 것 같다..백준 돌리면 바로 틀린다..
# 최단 거리 유형을 많이 풀어보면서 파악해야 한다. (거리를 더하는 것)

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int,input().split())
# 도시개수 = N , 도로개수 = M
# 거리 정보 = K , 출발 도시 번호 = X
graph=[[0] for _ in range(N+1) ]
# print(graph)
for i in range(1,M+1):
    A,B = map(int,input().split())
    graph[A].append(B)
# print(graph)
queue = deque([X])
# queue.append(X)
# recursive_list = graph[X][1:]
check = True

while K != 0:
    s = queue.popleft()
    recursive_list = graph[s][1:]
    for idx,i in enumerate(recursive_list):
        queue.append(i)
    K-=1
    if(K<=0):
        if(s == N):
            check = False
            break
    s = queue.popleft()
    recursive_list = graph[s][1:]
    if(len(recursive_list)==0):
        check = False
        break
    for j in recursive_list:
        queue.append(j)
        count = queue.count(j)
        if(count != 1):
            while j in queue:
                queue.remove(j)
    K-=1

if(K!=0 or check==False):
    print(-1)
else:
    queue = sorted(queue)
    for data in queue:
        print(data)
        
# 답지 코드
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int,input().split())
# 도시개수 = N , 도로개수 = M
# 거리 정보 = K , 출발 도시 번호 = X
graph=[[] for _ in range(N+1)]

for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)
distance[X] = 0 # 출발 도시까지의 거리는 0으로 설정

# BFS 수행
queue = deque([X])

while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            queue.append(next_node)
    
    # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        check = True
    # 만약 최단 거리 K 도시가 없다면, -1 출력
if check == False:
    print(-1)
