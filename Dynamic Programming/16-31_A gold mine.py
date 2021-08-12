# board를 만드는 것 부터 빈 칸 기준으로 한 줄로 다 받는 것은 처음이라, 어떻게 해야할지 애먹었다.
# dp 테이블을 n,m 인덱스를 기준으로 2차원 배열로 만들고, 그 2차원 배열을 가지고, 각 경우에 따라 나눈다.
# 30분안에 못 풀어서 코드에 주석을 추가하면서 그냥 이해하면서 짚어갔던 문제다.

# 답지 참고 풀이

import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n, m = map(int,input().split())
    board = list(map(int,input().split())) 
    dp = []
    idx = 0
    for i in range(n):
        dp.append(board[idx:idx+m])
        idx += m
    # print(dp)
    for i in range(1,m):
        for j in range(n):
            # 왼쪽 위
            if(j==0):  # 인덱스 오류 예외처리
                left_up =0  # j 가 현재 0 이면 left_up은 없다.
            else: # 그 외
                left_up = dp[j-1][i-1] # 왼쪽 위 값이 left_up 값
            # 왼쪽 아래로부터
            if(j==n-1):      
                left_down = 0
            else:
                left_down = dp[j+1][i-1]
            # 왼쪽으로부터 (i 가 1 부터 시작하므로 상관 x)
            left = dp[j][i-1]       
            dp[j][i] = dp[j][i] + max(left_up,left,left_down)
    
    answer = 0
    for i in range(n):
        answer = max(answer,dp[i][m-1])
    
    print(answer)
