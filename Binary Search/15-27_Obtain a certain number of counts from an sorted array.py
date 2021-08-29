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
    
# 이진 탐색 라이브러리 bisect를 활용한 방법 -- 답지풀이
from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

def count_by_range(array,left_value,right_value):
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index

n, x = map(int,input().split())
array = list(map(int,input().split()))
# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count_list = count_by_range(array,x,x)
# 값이 x인 원소가 존재하지 않는다면
if count == 0 :
    print(-1)
else:
    print(count)
    
