# 내가 푼 방법 


import sys
input = sys.stdin.readline

n = int(input())
fear_list = list(map(int, input().split()))
sorted_fear_list = sorted(fear_list)   # 맨 처음에는 오름차순이 아니라 내림차순으로 풀었다가 그룹수의 최댓값을 구하는 것이므로 오름차순으로 풀어야 한다.

group = 0   # 그룹 수
count = 0
for fear in sorted_fear_list:
    count += 1  # 최소 count가 1 이므로 1 일단 증가
    if count >= fear:  # count가 fear보다 크거나 같으면
        group += 1   # group 형성
        count = 0   # count 초기화

print(group)
