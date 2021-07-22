# 맨 처음에, 계속 틀렸다. (삼중 for문을 했어야 했는데, 2중 for문으로 풀었었다.)
# 결론은 역시 틀렸다.

import sys
from itertools import combinations
input = sys.stdin.readline

N,M  = map(int,input().split())  # 1<=M <=13
board = [list(map(int,input().split())) for _ in range(N)]
# 집 : 1 , 치킨집 : 2  
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j]== 1 :
            house.append([i,j])
        elif board[i][j] == 2 :
            chicken.append([i,j])

# 최대 M 개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력
choose_chicken = list(combinations(chicken,M))

min_list = [0]*len(choose_chicken)

for i in house:
    for j in range(len(choose_chicken)):
        # max_value = float('-inf')로 한다.
        min_value = float('inf') # 파이썬에서 inf 는 어떤 숫자와 비교해도 무조건 크다.
        for k in choose_chicken[j]:
            temp= abs(i[0]-k[0])+abs(i[1]-k[1])
            min_value=min(min_value,temp)
        min_list[j]+=min_value

print(min(min_list))
