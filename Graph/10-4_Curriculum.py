# 위상 정렬 기본 문제,,,
from collections import deque
import copy
import sys
input = sys.stdin.readline

n = int(input())
indegree = [0] *(n+1)
graph =[[] for i in range(n+1)]
# 각 강의 시간을 0으로 초기화
time = [0] *(n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    time[i] = data[0] # 첫 번쨰 입력한 수는 그 강의시간의 정보를 담고 있다.
    for x in data[1:-1]:
        indegree[i] +=1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    queue = deque() 

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,n+1):
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now] + time[i])
            indegree[i] -=1
            if indegree[i] == 0 :
                queue.append(i)
    
    for i in range(1,n+1):
        print(result[i])

topology_sort()
