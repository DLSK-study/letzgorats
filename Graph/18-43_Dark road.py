# 최소 신장 트리 구하는 것인데, 전체 비용에서 최소신장트리의 비용을 빼면 된다.
# 내가 푼 방법 -- 맞았긴 한데, 다음에도 풀고 맞아야 한다. 지금 머릿속에 계속 그래프 문제의 로직이 반복된다.

import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b 
        
n,m = map(int,input().split())
parent = [0] *n
for i in range(n):
    parent[i] = i

edges = []
total_cost = 0
for _ in range(m):
    x,y,z=map(int,input().split())
    total_cost += z
    edges.append((z,x,y)) # z 기준으로 정렬하기 위함
print(total_cost)
    
edges.sort()
result = 0
for edge in edges:
    cost, x,y = edge
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        result += cost
# print(result)
print(total_cost-result)
