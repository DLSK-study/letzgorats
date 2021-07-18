# 내가 푼 방법
import sys
input = sys.stdin.readline

S = sorted(list(input().rstrip())) # 문자열을 받으면 리스트 형태로 변환하고 바로 정렬해서 S 에 할당
# 정렬을 하면, 문자열은 아스키 코드 순으로 정렬된다.
sum = 0
answer = ''
for s in S:
    if(ord(s) < 65):  # 대문자 알파벳 A는 아스키코드가 65이므로 65를 기준으로 앞 뒤로 분기한다.
        sum += int(s)  # 숫자면 int로 형변환 하고 더함
    else:
        answer += s  # 문자면 answer에 붙인다. ( 앞서 정렬을 했기 때문에, 따로 또 정렬을 안해도 정렬이 되어 있다)
print(answer+str(sum)) # 문자+숫자 이어 붙인다.

''' 숫자 아스키코드는 숫자 그대로가 아니었다. 
숫자 아스키코드는 잘 몰라서 찾아보니 
0은 48 이고 9는 57 로 48~ 57 이라고 한다.'''
