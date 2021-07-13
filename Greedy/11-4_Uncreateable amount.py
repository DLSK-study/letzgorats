# 내가 푼 방법
-> 리스트에 있는 모든 수를 이용해서 만들 수 있는 수들을 새로운 리스트에 저장하려고 했으나,
도무지 방법이 안나와서 못풀었다.

# 해답을 참고한 풀이 
import sys
input = sys.stdin.readline

N = int(input())
coin_list = list(map(int, input().split()))
sorted_coint_list = sorted(coin_list)   # 오름차순으로 정렬

if_possible = 1   # 만들 수 있는 금액 : 초기값 1 원
for i in sorted_coint_list:
    if i > if_possible:  # 동전 i 가 if_possible보다 작거나 같지 않으면(크면) break
        break
    else:
        # 여기서 중요한 점은 else문으로 온 이상 possible-1 전까지는 금액을 만들 수 있다는 것을 의미한다.
        if_possible += i

# 빠져나온 if_possible 값을 그대로 출력(빠져나온 if_possible 값은 못 만드는 금액이라는 뜻)
print(if_possible)

