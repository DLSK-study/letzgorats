# 맨 처음에, dp테이블의 모든 값을 -1 로 초기화 해줘서, 대수비교에서
# 예외처리가 너무 까다로웠다.
# 처음 풀었던 풀이는 아래와 같다. 풀긴 풀었다.(시간약간 오바)
import sys
input = sys.stdin.readline

coin = []
n,m = map(int,input().split())
for _ in range(n):
    coin.append(int(input()))
dp = [-1] * 10001
for x in coin :
    dp[x] = 1

for x in coin:
    for i in range(2,m+1):
        if(i in coin):  # coin 리스트(화폐 리스트)에 있으면 pass
            continue
        if(dp[i]!=-1):  # dp[i] 가 -1이 아니라면
            if(dp[i-x]!=-1):  # dp[i-x] 가 -1 이 아니면
                dp[i] = min(dp[i-x]+1,dp[i])  # i에서 이번에 탐색하는 x를 빼준 dp[i-x]+1 과 전에 저장되었던 dp[i] 중에 작은 값을 선택 
        if(dp[i-x]!=-1): # dp[i-x] 가 -1 이 아니라면,
            if(dp[i]!=-1):  # dp[i] 가 -1 이 아니라면, 똑같이
                dp[i] = min(dp[i-x]+1,dp[i])
            else:  # dp[i]가 이제 처음이라면
                dp[i] = dp[i-x]+1  # dp[i-x] +1 을 해준다. 
# if문에 걸리지 않은 경우는 그냥 초기값 -1 
print(dp[m])


# 30분이 넘어서, 살짝 답지를 봤는데, 10001이라는 숫자로 초기화 해준 것만 보고 다시 고쳤는데, 바로 깔끔하게 됐다.
# 최소값을 선택해야 할 때, 무한의 큰 값으로 초기화 해주면, 해결할 수 있는 문제였다.
# 마지막으로, dp[m]의 값이 여전히 초기값 10001 과 같다면, -1을 출력해주면 되는 문제였다.
# 아쉽다.

import sys
input = sys.stdin.readline

coin = []
n,m = map(int,input().split())
for _ in range(n):
    coin.append(int(input()))
dp = [10001] * 10001
for x in coin :
    dp[x] = 1

for x in coin:
    for i in range(2,m+1):
        if(i in coin):
            continue
        elif(dp[i-x]!=10001):
            dp[i]=min(dp[i],dp[i-x]+1)
if(dp[m]==10001):
    print(-1)
else:
    print(dp[m])
    
    
