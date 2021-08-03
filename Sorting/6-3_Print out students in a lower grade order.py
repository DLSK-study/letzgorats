import sys
input = sys.stdin.readline

n = int(input())
info = {}
for i in range(n):
    name , score = input().split()
    info[name] = int(score)
info = sorted(info.items(),key = lambda x : x[1])

for s in info: 
    print(s[0],end=" ")
    
