# 정확도는 맞지만, 백준 돌리면 시간초과가 나온다,,
# 너무 함수를 많이 짠 것 같다.
# 테스트 케이스 성공은 다 맞다.
'''
테스트 케이스 1 ( O )
6 16
4 7 8 0 6 16 
0 13 0 0 0 12
14 0 0 1 0 3
0 0 9 0 0 15
0 0 5 0 11 0
2 0 0 10 0 0
4 5 4

결과값 : 5

테스트 케이스 2 ( O )
5 4
1 2 2 2 3
2 0 0 3 0
3 2 0 0 0
3 3 0 4 0
2 2 2 1 0
2 4 3

결과값 : 2

'''

import sys
from collections import deque
import copy
input = sys.stdin.readline

def spread_virus(x,y,graph):   # 바이러스 퍼뜨리는 함수
    # print(graph,"**")
    for i in range(4):
        nx = x+dr[i]
        ny = y+dc[i]
        if(nx >=0 and ny >=0 and nx < N and ny < N ):
            if(graph[nx][ny]==0):  # 시험관 위치가 바이러스 위치 기준으로 상 하 좌 우 가 0 이면 
                graph[nx][ny]=graph[x][y]    # 퍼뜨린다.
            # 바이러스 리스트에 있는 바이러스 순으로 한번 퍼뜨렸는데, 그 먼저 퍼뜨렸던 바이러스 순위가 현재 퍼뜨리려고 하는 바이러스 
            # 순위보다 높다면, (즉, 현재 바이러스 퍼뜨리려고 하는 값이 더 작다면) 
            # 그리고, 초 단위로 업데이트되는 바이러스가 퍼진 시험관에서의 위치가 바이러스가 있는 위치가 아니라면,
            elif(graph[nx][ny] != 0 and graph[nx][ny] > graph[x][y] and wall_graph[nx][ny]==False):  
                graph[nx][ny]=graph[x][y]  # 그 위치는 새로운 바이러스 값으로 업데이트
    # print(graph)
    return graph 

def update_virus(graph):   # 감염 유효한 바이러스 위치 업데이트(바이러스 상하좌우에 바이러스 있으면 소용 X) 
    for i in range(N):
        for j in range(N):
            if(graph[i][j] == 0):  # update_virus는 청정지역을 기준으로 상하 좌우에 바이러스 요효값을 
                for k in range(4):
                    ni = i+dr[k]
                    nj = j+dc[k]
                    if(ni >=0 and nj >=0 and ni < N and nj < N):
                        if(graph[ni][nj]==0):
                            pass
                        else:
                            virus_list.append([ni,nj])  # 새로운 바이러스 리스트에 추가해준다.

    return virus_list  # 바이러스 리스트 다시 반환

def update_graph(graph):  # 시험관 업데이트
    update_graph = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if(graph[i][j]!=0):
                update_graph[i][j]=True
    return update_graph

def select_virus(count,graph,virus_list):
    if(count == S):  # 입력한 시간에 다다르면 그대로 현재 시험관 출력
        return graph

    for num in range(len(virus_list)): # 현재 유요한 바이러스 리스트에 저장된 길이 만큼 돌고 
        x,y = virus_list[num]    # 각각의 유효한 바이러스 리스트에 저장된 좌표값 x,y로 뽑고
        # visited[x][y]=True
        graph = spread_virus(x,y,graph) # 현재 시험관에서 바이러스 퍼뜨린다.

    # for문 다 돌았다는 것은 규칙에 맞게 virus 다 퍼졌다는 것이다.

    virus_list.clear()
    virus_list = update_virus(graph)

N,K = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))
S,X,Y = map(int,input().split()) # S초 후 , (X,Y) 위치 바이러스 종류 출력
dr = [-1,1,0,0] # 상 하 좌 우 
dc = [0,0,-1,1] # 상 하 좌 우
virus_list = []
visited = [[False]*N for _ in range(N)]

update_virus(graph)  # 초기 바이러스 좌표 리스트 업데이트
wall_graph = update_graph(graph)  # 초기 바이러스 위치 업데이트(바이러스 있는 자리는 True) 
# print(virus_list,"vv")

count = 0 # 0 초부터 시작 
while S!=count:
    select_virus(count,graph,virus_list)  #  1초 동안 현재 시험관에서 바이러스 퍼뜨린다.
    count+=1 # 1초 흐름
    wall_graph = update_graph(graph) # 현재 시험관 기준으로 바이러스 위치는 True, 청정지역은 False
    if(all(wall_graph)):  # 이미 모두 다 퍼졌다면, 더 이상 시간 진행 안해도 된다.
        break
    # print(count,"cccc")

print(graph[X-1][Y-1]) 
