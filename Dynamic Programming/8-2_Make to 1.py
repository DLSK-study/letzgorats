# 내가 처음에 풀었던 방법
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 30001

for i in range(2,n+1):
    if(i%5==0):
      dp[i] = min(dp[i],dp[i//5]+1)   # min 한 이유는 12나 15와 같이 중복되는 배수인 경우도 있고, min이 없으면, 중간에 값이 무조건 마지막 조건문에 따라 정해진다.
    if(i%3==0):
      dp[i] = min(dp[i//3]+1,dp[i])
    if(i%2==0):
      dp[i] = min(dp[i],dp[i//2]+1)
    else:
      dp[i] = dp[i-1]+1

print(dp[n])
# 이렇게 푸니까 계속 0 이 나왔다. 

# 예외처리를 해준 코드는 다음과 같다.
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 30001

for i in range(2,n+1):
    if(i%5==0):
        if(dp[i]!=0):
            dp[i] = min(dp[i],dp[i//5]+1)
        else:
            dp[i] = min(dp[i-1]+1,dp[i//5]+1)
    if(i%3==0):
        if(dp[i]!=0):
            dp[i] = min(dp[i],dp[i//3]+1)
        else:
            dp[i] = min(dp[i-1]+1,dp[i//3]+1)  # 16 과 같은 예를 생각해줘야 하므로, dp[i]==0 인 경우, 우선 dp[i-1] 한 값 + 1 과 해당 수와 나눈 값 중 작은 값을 선택 
    if(i%2==0):
        if(dp[i]!=0):
            dp[i] = min(dp[i],dp[i//2]+1)
        else:
            dp[i] = min(dp[i-1]+1,dp[i//2]+1)
    if(i%2!=0 and i%3!=0 and i%5!=0):
        dp[i] = dp[i-1]+1

print(dp[n])



# 답지 코드 -- dp[i] = dp[i-1]+1 을 그냥 맨 앞에다 놔주면, 해결됐다..
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 30001

for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    
    if(i%5==0):
        dp[i] = min(dp[i],dp[i//5]+1)
    if(i%3==0):
        dp[i] = min(dp[i//3]+1,dp[i])
    if(i%2==0):
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[n])




