# 맨 처음에, 시작점과 끝점을 (떡의 최소 길이, 떡의 최대 길이) 로 잡았는데, 그러면, 예외처리를 앞서서 해줘야 했다.
# 고친 코드는 시작점을 0으로 하고 끝점을 떡의 최대 길이로 하면 됐다.
# 또한, target 길이와 자른 떡의 합이 같아지면 answer에 mid 값을 저장하고 while문을 탈출하면 된다.

import sys
input = sys.stdin.readline

def cut_tteok(start,end,target,tteok):
    global answer
    while start<=end:
        res = 0
        mid = (start+end)//2
        for x in tteok:
            if x > mid:
                res += x-mid
        print(res)
        if(target < res):
            answer = mid
            start = mid + 1
        elif(target > res):
            end = mid - 1
        else:
            answer = mid 
            break
        
n, m = map(int,input().split())
tteok = sorted(list(map(int,input().split())))
# print(tteok)
answer = 0
cut_tteok(0,max(tteok),m,tteok)
print(answer)
