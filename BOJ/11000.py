import heapq
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


n = int(input())

schedule = [list(map(int,input().split())) for _ in range(n)]
schedule.sort(key = lambda x : x[0])

q = []
heapq.heappush(q,schedule[0][1]) # 맨 처음 시작한 강의 끝나는 시간을 넣는다.

for i in range(1,n):
    if q[0] > schedule[i][0]: # q에 있는 시간이 스케쥴의 시작 시간보다 크면
        heapq.heappush(q,schedule[i][1]) # q에 끝나는 시간을 넣는다.
    else:
        heapq.heappop(q)
        heapq.heappush(q,schedule[i][1])

print(len(q))


'''
전체적으로 회의실배정 문제와 비슷한데 회의실 배정 문제에서는 필요없는 회의 시간을 버렸지만
이번 문제는 필요없는 강의 시간을 버리는 것이 아니라 큐에 다시 집어넣어
최종적으로 큐의 길이(강의실의 수)를 출력해준다

왜 그런지 토의해보자..
'''
