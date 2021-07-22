# 고려해야할 게 많아서 시간안에 못 풀었다,,
# 유튜브 풀이 : 테스트 : 50.4 / 100 
def testCol(bo,column,x,y):
    # 기둥을 세울 수 있는 경우 1) y가 0이면 항상 가능
    if y == 0:
        return True
    # 2) 기둥왼쪽,오른쪽에 보가 있는 경우 가능
    # 왼쪽 보의 좌표는 (x-1,y)가 되겠고, 오른쪽 보는 기둥과 좌표가 같다 (x,y)
    if x-1>= 0 and bo[x-1][y] == 1 :
        return True
    if bo[x][y] == 1:
        return True
    # 3) 밑에 기둥이 있는 경우 가능, 이 때, 밑의 기둥의 좌표는 (x,y-1)이다.
    if column[x][y-1]==1: # y=0 인 인덱스는 어차피 걸려졌기 때문에 y-1>=0 and~ 가 굳이 필요없는 것이다.
        return True
    return False

def testBo(bo,column,x,y,N):
    # 보를 설치할 수 있는 경우 1) 보 왼쪽 부분에 기둥이 있는 경우 가능, 보 오른쪽 부분에 기둥이 있는 경우 가능
    # 이 때, 보 왼쪽 기둥의 좌표는 (x,y-1) 가 되겠고, 보 오른쪽 기둥의 좌표는 (x+1,y-1)가 되겠다.
    if y-1>=0 and column[x][y-1] ==1 :
        return True
    if x+1<N and y-1>=0 and column[x+1][y-1]==1:
        return True
    # 2) 동시에 양쪽에 보가 존재하면, 가능하다.
    # 이 때 왼쪽 보의 좌표는 (x-1,y) 이고, 오른쪽 보의 좌표는 (x+1,y) 이다.
    if x-1>=0 and bo[x-1][y] ==1 and x+1 < N and bo[x+1][y]==1:
        return True
    return False

def solution(n, build_frame):
    N = n+1 # 인덱스가 n까지 사용되므로 n+1 이 필요하다. 
    column = [[0] * N for _ in range(N)]
    bo = [[0] * N for _ in range(N)]
    
    for x,y,a,b in build_frame:
        if b==1: # b가 1일 때, (설치)
            if a== 0 : # a가 0이라면, 기둥
                if testCol(bo,column,x,y) : # 기둥을 세울 수 있는지 판단하고 가능하면
                    column[x][y]=1
            else : # a가 1이라면, 보
                if testBo(bo,column,x,y,N):
                    bo[x][y]=1
        else : # b==0 , (삭제)
            if a== 0 : # a가 0이라면, 기둥
                # 3가지 경우) 
                # 일단 기둥 삭제해보고,
                column[x][y]=0
                # 1) 왼쪽에 보가 없거나 현재 위치에서 기둥을 삭제했을 때, 왼쪽보 설치가 가능한지 검증
                A = x-1>=0 and y+1 < N and (bo[x-1][y+1]== 0 or testBo(bo,column,x-1,y+1,N))
                # 2) 위에 기둥이 없거나, 현재 위치에서 기둥을 삭제했을 때, 위쪽 기둥이 설치가 가능한지 검증
                B = y+1 < N and (column[x][y+1] == 0 or testCol(bo,column,x,y+1))
                # 3) 오른쪽에 보가 없거나 현재 위치에서 기둥을 삭제했을 때, 오른쪽 보 설치가 가능한지 검증
                C = y+1 < N and (bo[x][y+1]== 0 or testBo(bo,column,x,y+1,N))
                test = A & B & C
                if test is False: # 성립할 수 없다면,
                    # 다시 복원한다.
                    column[x][y]=1
            else : # a가 1이라면, 보
                # 4가지 경우)
                # 일단 보를 삭제해보고,
                bo[x][y]=0
                # 1) 왼쪽에 있는 보가 없거나, 현재 위치에서 보를 삭제했을 때, 왼쪽 보가 설치가 가능한지 검증
                A = x-1>=0 and (bo[x-1][y] ==0 or testBo(bo,column,x-1,y,N))
                # 2) 왼쪽 위로 기둥이 없거나, 현재 위치에서 보를 삭제했을 때, 왼쪽 위로 기둥을 설치하는 것이 가능한지 검증
                B = column[x][y]==0 or testCol(bo,column,x,y)
                # 3) 오른쪽 위로 기둥이 없거나, 현재 위치에서 보를 삭제했을 때, 오른쪽 위로 기둥을 설치하는 것이 가능한지 검증
                C = x+1 < N and (column[x+1][y]==0 or testCol(bo,column,x+1,y))
                # 4) 오른쪽에 보가 없거나, 현재 위치에서 보를 삭제했을 때, 오른쪽 보가 설치가 가능한지 검증
                D  = x+1 < N  and (bo[x+1][y] ==0 or testBo(bo,column,x+1,y,N))
                test = A & B & C & D
                if test is False: # 성립할 수 없다면,
                    # 다시 복원한다.
                    bo[x][y]=1
    
    answer = []
    for i in range(N):
        for j in range(N):
            if column[i][j] ==1 : # 기둥이 있다면
                answer.append([i,j,0]) # 기둥은 0 
            if bo[i][j] == 1 : # 보가 있다면
                answer.append([i,j,1]) # 보는 1 
    
    return answer

# n이 5이상 100 이하인 자연수이기 때문에, 검증 조건을 모든 좌표를 다 검사하는 것으로 바꿔도 시간초과가 안난다.

def testCol(bo,column,x,y):
    # 기둥을 세울 수 있는 경우 1) y가 0이면 항상 가능
    if y == 0:
        return True
    # 2) 기둥왼쪽,오른쪽에 보가 있는 경우 가능
    # 왼쪽 보의 좌표는 (x-1,y)가 되겠고, 오른쪽 보는 기둥과 좌표가 같다 (x,y)
    if x-1>= 0 and bo[x-1][y] == 1 :
        return True
    if bo[x][y] == 1:
        return True
    # 3) 밑에 기둥이 있는 경우 가능, 이 때, 밑의 기둥의 좌표는 (x,y-1)이다.
    if column[x][y-1]==1: # y=0 인 인덱스는 어차피 걸려졌기 때문에 y-1>=0 and~ 가 굳이 필요없는 것이다.
        return True
    return False

def testBo(bo,column,x,y,N):
    # 보를 설치할 수 있는 경우 1) 보 왼쪽 부분에 기둥이 있는 경우 가능, 보 오른쪽 부분에 기둥이 있는 경우 가능
    # 이 때, 보 왼쪽 기둥의 좌표는 (x,y-1) 가 되겠고, 보 오른쪽 기둥의 좌표는 (x+1,y-1)가 되겠다.
    if y-1>=0 and column[x][y-1] ==1 :
        return True
    if x+1<N and y-1>=0 and column[x+1][y-1]==1:
        return True
    # 2) 동시에 양쪽에 보가 존재하면, 가능하다.
    # 이 때 왼쪽 보의 좌표는 (x-1,y) 이고, 오른쪽 보의 좌표는 (x+1,y) 이다.
    if x-1>=0 and bo[x-1][y] ==1 and x+1 < N and bo[x+1][y]==1:
        return True
    return False

def solution(n, build_frame):
    N = n+1 # 인덱스가 n까지 사용되므로 n+1 이 필요하다. 
    column = [[0] * N for _ in range(N)]
    bo = [[0] * N for _ in range(N)]
    
    for x,y,a,b in build_frame:
        if b==1: # b가 1일 때, (설치)
            if a== 0 : # a가 0이라면, 기둥
                if testCol(bo,column,x,y) : # 기둥을 세울 수 있는지 판단하고 가능하면
                    column[x][y]=1
            else : # a가 1이라면, 보
                if testBo(bo,column,x,y,N):
                    bo[x][y]=1
        else : # b==0 , (삭제)
            if a== 0 : # a가 0이라면, 기둥
                # 3가지 경우) 
                # 일단 기둥 삭제해보고,
                column[x][y]=0
                test = True
                for i in range(N):
                    for j in range(N):
                        test &= bo[i][j] == 0 or testBo(bo,column,i,j,N)
                        test &= column[i][j] == 0 or testCol(bo,column,i,j)
                if test is False: # 성립할 수 없다면,
                    # 다시 복원한다.
                    column[x][y]=1
            else : # a가 1이라면, 보
                # 4가지 경우
                # 일단 보를 삭제해보고,
                bo[x][y]=0
                test = True
                for i in range(N):
                    for j in range(N):
                        test &= bo[i][j] == 0 or testBo(bo,column,i,j,N)
                        test &= column[i][j] == 0 or testCol(bo,column,i,j)
                if test is False: # 성립할 수 없다면,
                    # 다시 복원한다.
                    bo[x][y]=1
    
    answer = []
    for i in range(N):
        for j in range(N):
            if column[i][j] ==1 : # 기둥이 있다면
                answer.append([i,j,0]) # 기둥은 0 
            if bo[i][j] == 1 : # 보가 있다면
                answer.append([i,j,1]) # 보는 1 
    
    return answer
