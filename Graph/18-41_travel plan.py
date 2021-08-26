# 여행 계획이 한 집합에 속하면 가능한 여행 계획 -- union, find 를 적절히 사용하면 풀 수 있는 문제였다. 다만, 다음에도 풀 때 바로 풀 수 있는지가 관건

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
graph=[[] for _ in range(n+1)]
# print(graph)
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i 

for i in range(1,n+1):
    row = list(map(int,input().split()))
    graph[i].append(row)
    for j in row:
        if j==1:
            union_parent(parent,i,j+1)    # 각 나라를 연결
        

trip_plan = list(map(int,input().split()))
possible = True
for idx,city in enumerate(trip_plan[:-1]):
    if(find_parent(parent,city) != find_parent(parent,trip_plan[idx+1])):  # 여행계획의 나라의 부모가 같지 않으면 다른 집합
        possible = False

if(possible==True):
    print("YES")
else:
    print("NO")    
