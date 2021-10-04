# 누적합,,
import sys
input = sys.stdin.readline

n,k,b = map(int,input().split())  # 신호등 개수 , 연속으로 켜져있어야 하는 신호등 개수, 고장난 신호등 개수 
broken_list = [0 for _ in range(n+1)]  # 모든 신호등을 0으로 초기화
for _ in range(b):  # 고장난 신호등은 1로 재설정
    traffic_light = int(input())
    broken_list[traffic_light] = 1

for i in range(1,n+1):  # 1번 신호등부터 n번 신호등까지 고장난 신호등 개수의 누적합을 구한다.
    broken_list[i] += broken_list[i-1]

answer = b  # 수리해야 할 신호등은 b를 초과할 수 없다.

for i in range(k,n+1):
    answer = min(answer,broken_list[i]-broken_list[i-k])
print(answer)
'''
이제 k 부터 탐색을 하여 
현재 인덱스에서 k 이전의 고장난 신호등 개수를 빼준다.
그렇다면 해당 k개의 "연속된 구간"에서 수리해야 할 신호등의 개수가 될 것이고
이를 최솟값 비교를 한다.
'''
