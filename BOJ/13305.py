# 작년에 풀었던 문제였다.
import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))[:-1] # 마지막 가격은 필요가 없다.
answer = 0
now_p = int(1e9)

for i in range(n-1):
    if(now_p > prices[i]):  # 순회하는 가격이 now_p에 저장되어 있는 가격보다 저렴하다면
        now_p = prices[i]   # now_p 갱신하고
        answer += now_p * roads[i]  # answer에 해당 주유비를 더한다.
    else:  # now_p 에 저장되어 있는 가격이 더 저렴하면
        answer += now_p * roads[i]  # 그대로 주유비 계산에서 더해준다.
print(answer)


# 작년에 나의 풀이
n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_Price = prices[0]

total = 0
for i in range(n-1):
    if i == 0:
        total += prices[0] * roads[0]
        min_Price = min(min_Price, prices[i])
    else:
        min_Price = min(min_Price, prices[i])
        total += min_Price * roads[i]
print(total)
