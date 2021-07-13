# 내가 푼 방법 -- 처음에 틀림, 반례 발견 : 11111

import sys
input = sys.stdin.readline

s = input()
s = s.replace('0', '').strip()  # 어차피 0은 더해야 하니까 곱하면 안되므로 그냥 없애주면 된다.
answer = 1
for num in s:
    answer *= int(num)
print(answer)


# 고친 방법 : 0은 없애주되, 1은 곱하는 것보다 더하는 것이 더 값이 크게 나옴
# 두번째도 틀린 방법, 반례 발견 : 12102

import sys
input = sys.stdin.readline

s = input()
s = s.replace('0', '').strip()  # 어차피 0은 더해야 하니까 곱하면 안되므로 그냥 없애주면 된다.
answer = int(s[0])
for num in s[1:]:
    if(num == '1'):
        answer += int(num)
    else:
        answer *= int(num)
print(answer)


# 고친 방법 : 그냥 단순하게 앞에서부터 뒤로 읽으면서 최종 answer에 더한 값이 곱한값 보다 크면 더해주고 작으면 곱해줌. 
import sys
input = sys.stdin.readline

s = input()
s = s.replace('0', '').strip()  # 어차피 0은 더해야 하니까 곱하면 안되므로 그냥 없애주면 된다.

answer = int(s[0])  # 초기값은 맨 처음 숫자

for num in s[1:]:
    if(int(num)*answer < int(num)+answer):
        answer += int(num)
    else:
        answer *= int(num)
print(answer)

