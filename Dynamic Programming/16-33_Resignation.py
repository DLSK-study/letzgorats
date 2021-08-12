# n 을 벗어나는 것을 처리하기 위해 n부터 0 으로 거꾸로 반복문을 도는 것이 핵심이었다.
# 역시 최댓값은 비교를 위해 초기값을 0으로 설정한다.
# 풀듯 말듯 하다가, 시간 초과나서 그냥 답지 참고했다,,

import sys
input = sys.stdin.readline

n = int(input())
schedule = []
dp=[0]*(n+1)
for i in range(n):
    schedule.append(list(map(int,input().split())))
# print(schedule)
for i in range(n-1,-1,-1):
    if(i+schedule[i][0]>n):  # 벗어나면
        dp[i] = dp[i+1]  # dp[i+1] 유지
    else:
        dp[i] = max(dp[i+1],dp[i+schedule[i][0]]+schedule[i][1]) 
print(dp[0]) # 쭉쭉 가면 0번째 index 가 최대 수익
