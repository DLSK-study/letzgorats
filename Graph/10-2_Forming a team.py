# 기본문제
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

for _ in range(m):
    operator, a,b  = map(int,input().split())
    if(operator==0):
        union(parent,a,b)
    elif(operator==1):
        if(find(parent,a)==find(parent,b)):
            print("YES")
        else:
            print("NO")
