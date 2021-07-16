
'''단순하게 풀어서는 효율성 테스트를 절대 통과할 수 없다.
   food_times의 길이와 원소를 크게 줬기 때문에 복잡도가 낮은 더 효율적인 방법을 찾아야 한다. 
   이 코딩테스트의 정확성 테스트 정답률은 42.08% 인 반면, 효율성 테스트의 정답률은 5.52% 였던 만큼, 효율성 측면에서는 쉽지 않았던 문제이다.'''

# 내가 푼 방법 중 틀렸던 방법 -- 정확성 테스트 : 33.5 / 효율성 테스트 : 0 --> 아예 다른 방법으로 풀어야 한다.
def solution(food_times, k):
    total = sum(food_times)
    if(total<=k):
        return -1
    else:
        time = 0
        idx = 0
        while True:
            for idx in range(len(food_times)):
                change_index = False
                if(food_times[idx]==0): 
                    continue
                food_times[idx]-=1
                time+=1
                if(idx+1>=len(food_times)):
                    idx=(idx+1)%len(food_times)
                    change_index = True 
                if(time==k):
                    if(change_index==True):
                        while(food_times[idx]<=0):
                            idx+=1
                            if(idx+1>=len(food_times)):
                                idx=(idx+1)%len(food_times)
                            else: idx+=1
                        return idx+1 
                    elif(change_index==False):
                        idx += 1
                        while(food_times[idx]<=0):
                            idx+=1
                            if(idx+1>=len(food_times)):
                                idx=(idx+1)%len(food_times)
                            else: idx+=1
                        return idx+1
                    
# 효율적인 코드 - 유튜브 참고 
from operator import itemgetter

def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i],i+1)) # 튜플 형태로 저장하는데, 첫번째 값이 음식섭취시간, 두번째 값을 음식번호로 저장한다.
    
    foods.sort() # 음식섭취 시간 순으로 오름차순 정렬된다.
    
    pretime = 0 # 이전 음식시간과의 diff - 초기값: 0
    
    for i, food in enumerate(foods):
        diff = food[0]-pretime  # diff는 높이라고 생각해라.
        if(diff!=0):
            spend = diff * n # 소비한 시간은 (diff x 남은음식)        
            if (spend<=k):
                k-=spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:],key = itemgetter(1))
                return sublist[k][1]  # 그 음식의 번호를 return 해야 하므로 인덱스 1을 가져온다.
        
        n-=1 # 턴이 하나 끝날 때마다 음식 하나를 다 먹은 것이므로 n-1을 해준다.
        
    return -1
                      

# heapq 사용한 방법
import heapq

def solution(food_times, k):
    n = len(food_times)  # 전체 음식시간 길이
    hq = [] # heapq 넣을 곳
    for i in range(n):
        # 힙큐에 튜플 형태로 넣어줌 (음식먹는시간,음식번호)
        heapq.heappush(hq,(food_times[i],i+1))
    
    pre_food = 0 #가장 밑바닥
    min_food = hq[0][0] # 현재 음식중 가장 작은 녀석
    
    # 사이클을 돌면서 k에서 시간을 계속 빼준다.
    while True :
        # 사이클 돌았을 때, k가 음수가 되면 탈출
        if (k-(min_food-pre_food)*n)<0:
            break
        
        # 아니라면 k 빼주고
        k -=(min_food-pre_food)*n
        
        # 힙큐에서도 그 음식을 빼준다.
        heapq.heappop(hq)
        pre_food = min_food # 바닥은 방금 그 음식의 양이다.
        n-=1 # 전체 길이도 하나 빼준다.
        
        # 만약 다 먹었는데도 k 가 남아있다면 음식이 부족한 상태이므로
        if not hq:
            return -1
        
        # 이것을 나중에 해주는 이유는 위에서 비어있을 경우 인덱스 에러가 나기 때문
        min_food = hq[0][0]
    
    # 전체 길이보다 남은 초가 더 많을 수 있으므로 
    # 초를 길이로 나눈 나머지가 답이다.
    idx = k % n
    # 다시 번호 순으로 정렬 해주고
    hq.sort(key=lambda x:x[1])
    answer = hq[idx][1]
    return answer
