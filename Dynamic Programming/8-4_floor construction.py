# 맨 처음에 dp[i] = (2*dp[i-1] + dp[i-2]) % 796796 로 풀었다.
# 예외가 너무 많이 생겼다,,,
# 결국, 내 스스로 못풀었다.

# 답지 풀이
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = 5
# dp[4] = 11
for i in range(3,n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2]) % 796796
print(dp[n])
