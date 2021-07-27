# 벽을 3개 세우는 것을 해결하지 못하엿다,,
# 구글링 코드,,
import sys
import copy
input = sys.stdin.readline

N, M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
graph_copy = copy.deepcopy(graph)

max_safe = 0

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1] # 상하좌우
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i,j])



def select_wall(start,count):
    global max_safe

    if count ==3 : # 벽 3개 선택 완료 됐으면,
        update_graph = copy.deepcopy(graph)
        for num in range(len(virus)):
            x,y = virus[num]
            spread_virus(x,y,update_graph)
        safe_count = sum(i.count(0) for i in update_graph) # clean 지역 count
        max_safe = max(max_safe,safe_count) # 기존 max_safe 과 safe_count 중 큰 것을 채택
        return True
    else:
        for i in range(start,N*M): # 2차원 배열에서 조합 구하기
            x = i // M 
            y = i % M
            if(graph[x][y]==0): # 안전영역인 경우 벽으로 선택 가능
                graph[x][y] = 1 # 벽으로 변경
                select_wall(i,count+1) # 벽 선택
                graph[x][y] = 0
def spread_virus(x,y,update_graph):
    if(update_graph[x][y]==2):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >=0 and ny>=0 and nx<N and ny < M :
                if update_graph[nx][ny]==0: # 벽을 만나면
                    update_graph[nx][ny]=2 # 2로 만들어주고
                    spread_virus(nx,ny,update_graph) #바이러스 퍼뜨린다.

select_wall(0,0)
print(max_safe)
