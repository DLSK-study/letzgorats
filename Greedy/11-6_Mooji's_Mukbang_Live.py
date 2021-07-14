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
                      
