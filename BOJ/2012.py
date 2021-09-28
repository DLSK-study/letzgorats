import heapq
import sys
input = sys.stdin.readline

n = int(input())
predict_list = [int(input()) for _ in range(n)]
predict_list.sort()
rank = 1 # 초기값은 1로 시작
queue = []

for r in predict_list:
    if r == rank:  # 현재 rank와 값이 같으면 
        rank += 1  # rank 만 1 증가
    else:   # 다르면,
        heapq.heappush(queue,r)  # heapq에 넣는다

answer = 0

while queue:  # 큐가 빌 때 까지
    num = heapq.heappop(queue)
    if num == rank:  # 현재 num이 rank와 같다면
        rank += 1  # rank 만 1 증가
    else:  # 다르면,
        answer += abs(rank - num) # 절댓값을 answer에 더해준다.
        rank += 1  # rank 1 증가 

print(answer)
