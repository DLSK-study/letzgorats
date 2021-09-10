# 휴먼 파이프라인 문제
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
work_time = list(map(int,input().split()))
work_time.sort()
optimal = int(-1e9)
for idx in range(n-1):
    optimal = max(optimal,work_time[0]*(idx+1)+work_time[idx+1]*(n-idx-1))
answer = (k // optimal)
if(k % optimal ==0):
    print(answer)
else:
    print(answer+1) # 남으면 1번 더 왔다갔다 해야 한다.
