# 에라토스테네스의 체로 풀어도 시간초과가 날 수 밖에 없다. 다른 방법을 생각해냈어야 하는데 결국 못풀었다.
# 구글링을 하면서, 이해가 잘되는 풀이를 참고했다.

import sys
import math
input = sys.stdin.readline

min_num , max_num = map(int,input().split())  
result = 0
validation = [1 for _ in range(min_num,max_num+1)]

# max값보다 작은 모든 제곱수의 목록 생성
squares = [v**2 for v in range(2,int(math.sqrt(max_num))+1)]
for square in squares:
    # min부터 max까지의 수 중, 해당 제곱수의 최소의 배수를 구한다.
    cur_idx = (math.ceil(min_num /square) * square) - min_num
    while cur_idx <= max_num - min_num :
        # 제곱의 배수인 경우 해당 idx의 validation값을 0으로 대체
        validation[cur_idx] = 0
        # 다음 제곱수의 index를 구한다.
        cur_idx += square

# 남은 1들의 개수가 제곱 ㄴㄴ 수의 개수가 된다.
result = sum(validation)
print(result)

# 출처 :  https://nerogarret.tistory.com/32
