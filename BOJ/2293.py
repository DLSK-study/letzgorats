# 동전 1문제
import sys
input = sys.stdin.readline

n, k =map(int,input().split())
dp = [0] * (k+1)
coin_list = sorted([int(input()) for _ in range(n)])

for c in coin_list:
    for i in range(c,k+1):
        if i==c:
            dp[i]+=1
        else :
            dp[i] += dp[i-c]
print(dp[k])
