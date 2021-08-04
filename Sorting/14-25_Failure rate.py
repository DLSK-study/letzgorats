# 맨 처음에 81.00/100.00 이 나왔다. 다시 고쳐서 통과했다. 
# 마지막에 final 배열을 정리하는 것에서 애 먹었다.
# 중간에, 그냥 애초에 N 을 이용해 for문을 도는 방법이 생각났는데, 하던 방법으로 밀고 나갔다. (20분안에는 못풀었지만 근접하게 풀긴 풀었다.) 

from collections import deque

def solution(N, stages):
    stages = sorted(stages)   # 단계를 오름차순으로 정렬한다.
    stages = deque(stages)    # 리스트를 덱으로 만든다.
    answer = {}   # answer 이라는 딕셔너리 생성
    while stages:       # stages 덱이 빌 때 까지 돈다.
        length = len(stages)   # 길이를 length 라는 변수로 받는다.
        data = stages[0]       # data라는 변수에 현재 stages의 첫번째 값을 할당한다.
        i = 0    
        cnt = 0   # 실패율 계산을 위한 cnt 변수( 각 num이 현재 몇개인지)
        if(data>N): break  # data, 즉 stages의 첫번째 값이 N보다 크면 그냥 while문 탈출한다.(어차피 결과에 영향 x)
        while(len(stages)!=0 and data==stages[i]):  # stages 길이가 0이 아니고(popleft()를 하면서 while문을 돌기 때문에 길이가 0이 될수도 있기 때문에, index오류를 막기 위함)
                                                     # data와 첫번째 값이 같을 때 까지 반복, 즉, popleft() 하면서 맨 앞 값이 다른 숫자나오면 탈출하게 되어있다.
            num = stages.popleft()
            cnt+=1
        fail=cnt/length   # 실패율 계산
        answer[num]=fail  # 현재 number를 키값으로 하고 fail(실패율)을 value 값으로 하는 answer 딕셔너리에 추가
    sorted_answer = sorted(answer.items(),key= lambda x:-x[1])  # value(실패율) 값을 기준으로 내림차순 정렬(-x[1]) 
    final = []  # final 이라는 빈 배열에 
    for i in range(len(sorted_answer)):   # 실패율이 내림차순으로 정렬된 sorted_answer 길이만큼 돌면서
        final.append(sorted_answer[i][0])  # 각 stage 를 추가한다.  그러면, 실패율이 높은 stage 부터 낮은 stage 순으로 (내림차순으로) final 배열에 들어가게 된다. 
    for j in range(1,N+1):  # 이제, 총 N 개의 stage 중에서 안 들어간 stage를 오름차순으로 넣게 된다.
        if j not in final:
            final.append(j)   #  만약 final에 들어가 있지 않은 stage가 있으면 그냥 넣어주면 된다.
        
    return final
