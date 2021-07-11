# 내가 푼 방법

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
number_list = [int(i) for i in input().split()]
sorted_number_list = sorted(number_list, reverse=True)    # 입력받은 number_list를 내림차순으로 정렬한다.

total = 0
for num in sorted_number_list[:2]:    # 내림차순으로 정렬된 number_list에서 어차피 앞선 두 숫자만 사용되므로 슬라이싱해준다. 
    if(m < k):                     # m이 k 보다 작아졌다면(두번째 num은 무조건 if문으로 들어간다.), num에 m을 곱해주고 마무리한다. 
        total += num*m
        break
    total += num*k*(m//k)   # 가장 큰 수를 k번 곱하는 작업이 (m//k)만큼 반복되므로 그만큼 곱해준다. 
    m %= k                 # 이제 남은 횟수는 m % k 만큼이다.
print(total)
