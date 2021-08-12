# 편집 거리 유형 숙지하자
# 맨 처음에는, dp 로 안 풀고 문자열을 탐색하면서, 경우의 수로 풀려고 했으나, 반례 발견
# daysun -> saturday 안됨
# 시간상 결국 답지 보고 이해했다.

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def edit_dist(a,b):
    n = len(a)
    m = len(b)
    # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
    dp = [[0] *(m+1) for _ in range(n+1)]
    # dp 테이블 초기 설정 (중요!)
    for i in range(1,n+1):
        dp[i][0] = i  # A-> 빈문자열
    for j in range(1,m+1):
        dp[0][j] = j # 빈문자열 -> B
    
    # 최소 편집 거리 계산
    for i in range(1,n+1):
        for j in range(1,m+1):
            # 문자가 같다면, ""왼쪽 위""에 해당하는 수를 그대로 대입
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: # 삽입(왼쪽), 교체(왼쪽 위), 삭제(위쪽) 중에서 최소 비용 대입
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
    return dp[n][m]

A = input()
B = input()

print(edit_dist(A,B))
