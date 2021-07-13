# 내가 푼 방법
import sys
input = sys.stdin.readline

count = 0
S = input().strip()

standard = S[0]    # 맨 처음 숫자 기준으로 잡고 
for text in S[1:]:  # 두번째 숫자부터 읽기 시작한다.
    if text == standard:      #  숫자가 같으면 건너뛰고
        continue
    else:         # 다르면 
        count += 1   # count+1
        standard = text   # standard는 바뀐 숫자로 갱신

if(count % 2 == 1):    # count가 홀수면
    print(count//2+1)    # 몫 + 1 이 답
else:
    print(count//2)   # count가 짝수면 몫이 답
