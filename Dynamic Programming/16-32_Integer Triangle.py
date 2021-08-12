# 금광 문제와 유사한 문제
# 각 경우에 따라 최댓값이 무엇인지 판단해서 dp 테이블에 저장한다.
# 30분 약간 초과.. 풀긴 풀었다.

import sys
input = sys.stdin.readline

n = int(input())
dp = []
for i in range(1,n+1):
    dp.append(list(map(int,input().split())))
# print(dp)
for i in range(1,n):
    index = i
    for j in range(index+1):  # i+1 전까지 j 를 돈다
        if(j==0):
            dp[i][j] += dp[i-1][j]  # j가 0이면 맨 왼쪽이므로 그대로 그 이전 행의 j 열의 값 더해줌
        elif(j==i):
            dp[i][j] += dp[i-1][j-1]  # i와 j 가 같으면 맨 오른쪽이므로 dp[i-1][j-1] 값 더해줌
        else:
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])  # 왼쪽 오른쪽 값 중 큰 값을 더해줌

print(max(dp[n-1])) # 마지막 행에서 가장 큰 값 추출
