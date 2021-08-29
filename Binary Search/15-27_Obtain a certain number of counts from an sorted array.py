# 내가 푼 방법 - 계수 정렬 사용
import sys
input = sys.stdin.readline

n, x = map(int,input().split())
count_list = [0] *(10000001)
for i in input().split():
    count_list[int(i)]+=1
if count_list[x] == 0 :
    print(-1)
else:
    print(count_list[x])
