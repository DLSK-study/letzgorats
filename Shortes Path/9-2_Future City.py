# 플로이드 알고리즘 기초 문제 
# 답안을 볼려고 한 것은 아니지만, 코드가 살짝 보여서 플로이드 워셜 알고리즘인 줄 알아버렸다 처음부터,,
# 기본 문제라 넘어가자.

import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값
n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
# print(graph)
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    graph[i][i] = 0

x, k = map(int,input().split()) 


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]    # k를 먼저 거쳐 x로 가야함 

# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if graph[a][b] == INF:
#             print(-1,end= " ")
#         else:
#             print(graph[a][b],end=" ")
#     print() 
if distance >= INF:
    print(-1)
else:
    print(distance)
