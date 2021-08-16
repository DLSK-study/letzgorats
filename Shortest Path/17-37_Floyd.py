# 플로이드 재복습 문제, 앞서서 개념문제도 너무 비슷한 걸 많이 쳐봐서
# 지금이야 쉽게 맞을 수 있었지만, 나중에 플로이드인걸 몰랐을 때 어떻게 되는지는 지켜봐야 한다.

import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

bus = int(input())
for i in range(bus):
    a,b,cost = map(int,input().split())
    graph[a][b] = min(graph[a][b],cost)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][k]+graph[k][b],graph[a][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end=" ")
    print()
