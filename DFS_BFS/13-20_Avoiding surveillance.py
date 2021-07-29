# 백준 돌렸을 때 112ms로 결국 답은 통과 했지만, 60분 시간안에 못 풀었다,,사실 뻘짓만 안했으면 시간안에 풀만했는데, 복기해보자.
# 1) 코드를 짜면서 비슷한 코드가 많아서 복붙을 하면서 짜서 오타가 많았다..(행 dr인데 dc를 준다거나 등등) 하나하나 디버깅하느라 시간을 잡아먹었다. 제대로 확인하자.
# 2) [선생님 좌표 덱]을 [순열 덱]으로 만든다음에, 또 그 반복문 안에서 하나하나씩 꺼내가면서 [선생님 좌표 덱]이 빌 때까지 반복문을 돌았다,, 너무 너무 경우의 수가 많아서 아닌가 했지만
# 그대로 밀고 나갔다. 아닌 건 다시 신중히 그려보면서 생각해야 겠다. (이거 때문에 고려해야 할 사항이 너무 많아져서 또 계속 구현하느라 시간 잡아먹었다.)
# (아닌 이유)
''' 어차피 [선생님 좌표 덱]이 빌 때 까지 반복하므로 굳이 그 [선생님 좌표 덱]을 [순열덱]으로 경우의 수를 확장 시킬 필요가 없었다. 나는 어떤 [선생님 좌표 덱] 안에있는 좌표값 중에 
    어느 좌표부터 시작하느냐에 따라 "YES"가 나올수도 있고 "NO"가 나올수도 있다고 생각했는데( count값이 3이 되면 반복문에서 나오니까, 혹시나 [선생님 덱]에
  좌표값이 남아있으면, 제대로 계산을 할 수 없게 되는 것 같아 그렇게 생각했는데) 코드상, count가 3 이 됐다는 것은 이미 장애물을 다 만들었고, 어차피, 장애물이 만들어진 
  맵을 또 dfs2로 돌기 때문에, 결국 안되는 것은 "NO"로 나오게 됐다. 이게 써보면서, 깨달았다...'''
# 3) 선생님 한명을 기준으로 빈 값과 (동 서 남 북)에 학생이 있으면 이미, "NO"다. 그 if count==3 을 방향을 바꿔주는 for문 안에도 넣어줌으로써 해결하였다.(반례 다 찾아도 안돼서 애먹었다..)
# 4) 전역변수로 선언된 변수값의 변화와 매개변수로 주어지는 인자값의 변화로 인한 결과를 잘 구분하자.
# 결론 : DFS/BFS 문제가 어떻게 푸는지 이제 감이 오고, 푸는 루틴도 비슷한 것 같은데, 시간안에 해결해야 하는 것이 문제다. 코드를 짜다가 정말 아닌 것 같으면 과감히 다른 방안을 생각해보고,
# 중간에 다른 변수들이 생각났을 때는, 기록해두는 습관을 가지자. 

# 내가 푼 방법
import sys
from collections import deque
input = sys.stdin.readline

def keep_direction(ntposx,ntposy,i,hallway):
    global count
    nx = ntposx + dr[i]
    ny = ntposy + dc[i]
    in_range = False
    while (0<= nx <n and 0<= ny< n):
        if(hallway[nx][ny] == 'X' or hallway[nx][ny] == 'o'):
            hallway[nx][ny]='o'
            nx += dr[i]
            ny += dc[i]
        else:
            in_range = True
            break

    if(in_range == True and hallway[nx][ny]=='S'):
        if(i==0 or i==2):
            hallway[nx+dr[i+1]][ny+dc[i+1]]='O'
            count +=1
        else:
            hallway[nx+dr[i-1]][ny+dc[i-1]]='O'
            count +=1
    return hallway

def dfs(hallway,teacher_pos):
    while teacher_pos: # 선생님 위치가 빌 때 까지 실행
        if count == 3:
            break
        tposx,tposy = teacher_pos.popleft()
        for i in range(4):
            if count == 3:
                break
            ntposx = tposx + dr[i]
            ntposy = tposy + dc[i]
            if(0<= ntposx <n and 0<= ntposy < n):
                if(hallway[ntposx][ntposy]=='X' or hallway[ntposx][ntposy]=='o'):
                    hallway[ntposx][ntposy]='o'
                    hallway = keep_direction(ntposx,ntposy,i,hallway)
    
    return hallway

def keep_direction2(nsposx,nsposy,i,hallway):
    nx = nsposx 
    ny = nsposy
    can_block = False
    while (0<= nx <n and 0<= ny< n):
        if(hallway[nx][ny] == 'X' or hallway[nx][ny] == 'o' or hallway[nx][ny] == 'S'):
            nx = nx + dr[i]
            ny = ny + dc[i]
        elif (hallway[nx][ny]=='O'):
            can_block = True
            return True
        elif (can_block == False and hallway[nx][ny] == 'T'):
            return False

    return True

def dfs2(hallway,student_pos):
    # if count == 3 :
    #     return 
    while student_pos: # 학생 위치가 빌 때 까지 실행
        sposx,sposy = student_pos.popleft()
        for i in range(4):
            nsposx = sposx + dr[i]
            nsposy = sposy + dc[i]
            if(0<= nsposx <n and 0<= nsposy < n):
                if(hallway[nsposx][nsposy]=='O'):
                    continue
                else:
                    if(hallway[nsposx][nsposy]=='T'):
                        return "NO" 
                    elif(keep_direction2(nsposx,nsposy,i,hallway)==False):
                        return "NO"
    return "YES"

n = int(input())
hallway = [input().split() for _ in range(n)]
# visited = copy.deepcopy(hallway)

dr = [-1,1,0,0] # 상 하 좌 우 
dc = [0,0,-1,1] # 상 하 좌 우

teacher_pos = deque([])
student_pos = deque([])
for i in range(n):
    for j in range(n):
        if hallway[i][j] == 'T':
            teacher_pos.append([i,j])
        elif hallway[i][j] == 'S':
            student_pos.append([i,j])
answer = "NO"
count = 0

graph_case = dfs(hallway,teacher_pos)
answer = dfs2(graph_case,student_pos)
if (answer=="YES"):
    print(answer)
else:
    print(answer)
####################################################################################################################################################################
# 답지 풀이 - combinations (나중에 한번 봐야겠다)
    
