# 살짝 답지를 참고해서 풀었다.
# 1 22 20 3 이라는 예시를 생각하면서 풀었다.
# 답지 참고 풀이

import sys
input = sys.stdin.readline

dp = [0]*101
n = int(input())
food = list(map(int,input().split()))
dp[0] = food[0]
dp[1] = max(food[0],food[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+food[i])  # 이 점화식을 맨 처음에 생각해냈는데, n이 홀수일 때만 적용되는 것이 아닌가 했다. (ex) 1 22 20 
                                          # 하지만, 어차피 dp[n] 을 구하는 것이기 때문에, 마지막 값까지 도달하는 것이 중요하다. 된다.
print(dp[n-1])
