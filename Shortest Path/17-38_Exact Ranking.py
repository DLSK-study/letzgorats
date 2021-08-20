# n이 작아서 플로이드로 바로 접근
# 풀긴 풀었는데, 최단 경로문제인 것을 알고 풀었기 때문에 다시 풀어보기

import sys
input = sys.stdin.readline

INF = int(1e9)
n , compare = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

for i in range(compare):
    a,b = map(int,input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

possible = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if(graph[i][j] == INF or graph[i][j] == INF):
            continue
        else:    # 해당 노드에 오는 루트든 가는 루트든 다 존재하면 
            count+=1
    if count == (n-1):   # count가 자기자신 노드를 향한 루트를 제외한 횟수 n-1 이면 +1
        possible +=1

print(possible) 
'''
오류
'''
# 고친 코드
import sys
input = sys.stdin.readline

INF = int(1e9)
n , compare = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

for i in range(compare):
    a,b = map(int,input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        print(graph[a][b],end=" ")
    print()

possible = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if(graph[i][j]==INF and graph[j][i]==INF):
            continue
        else:    # 해당 노드에 오는 루트든 가는 루트든 다 존재하면 
            count+=1
    if count == n:   # count가 자기자신 노드를 향한 루트를 제외한 횟수 n-1 이면 +1
        possible +=1

print(possible)
