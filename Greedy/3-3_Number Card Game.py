# 내가 푼 방법

import sys
import time
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n):
    row = list(map(int, input().split()))
    current_min = min(row)
    if i == 0:
        max_of_entire_min = current_min    # 우선 첫번째 입력받은 행의 최솟값은 전체 행렬의 최소값 중 최대값이다.

    else:
        if current_min > max_of_entire_min:    # 현재 행에서의 최소값이 기존의 max_of_entire_min보다 크면, max_of_entire_min을 갱신시켜준다.
            max_of_entire_min = current_min

print(max_of_entire_min)


