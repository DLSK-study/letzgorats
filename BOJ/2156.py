import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
# 6 10 13 9 8 1
cnt = 0 
if n==1:
    print(wine[0])
elif n==2:
    print(wine[0]+wine[1])
else:
    dp[0] = wine[0]
    dp[1] = wine[0]+wine[1]
    dp[2] = max(dp[1],wine[0]+wine[2],wine[1]+wine[2])
    for i in range(3,n):
        # wine[i]+wine[i-1]+dp[i-3]
        # 은 현재 위치의 wine을 마시고 그 이전의 위치의 wine도 마신 경우
        # wine[i]+dp[i-2]는 현재 와인을 마시고 그 이전의 위치의 wine을 마시지 않은 경우
        # dp[i-1]은 현재 와인을 아예 마시지 않은 경우(dp[i-1]가 더 커서)
        dp[i] = max(max(wine[i]+wine[i-1]+dp[i-3],wine[i]+dp[i-2]),dp[i-1])
    
    print(dp[n-1])
