import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0] *(n+1)
for i in range(0,n+1):
    parent[i] = i

edges = []
result = 0
max_cost = 0

for _ in range(m):
    a,b,cost  = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result+=cost 
        max_cost = cost

print(result-max_cost) # 최소 신장 트리 2개 인데, 마지막 가장 큰 cost를 빼야 최소 유지비
