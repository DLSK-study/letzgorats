# 어글리 넘버는 학부 수업 때도 다뤘던 예제이다. 해밍 수 구하기랑 똑같은 문제다.
# 푸는 방법은 많은 것 같다..
# 내가 푼 방법
import sys
input = sys.stdin.readline

base = [2,3,5]
now = [2,3,5]
index = [0,0,0]
hamming = [1]
n = int(input())
while True:
    num = min(now)
    if(len(hamming)==n):
        break
    hamming.append(num)
    for idx,uglynum in enumerate(now):
        if(uglynum == num):
            index[idx]+=1
            now[idx]=base[idx]*hamming[index[idx]] # 여기 식 짜느라,애 먹었다,, 30분 살짝 초과했다..
print(hamming[-1])


# 답지 참고 코드
import sys
input = sys.stdin.readline

n = int(input())
dp=[0]*(n)

dp[0] = 1
next2,next3,next5 = 2,3,5
i2=i3=i5 = 0  
for i in range(1,n):
    dp[i] = min(next2,next3,next5)
    if(dp[i]==next2):
        i2 +=1
        next2 = dp[i2]*2   
    if(dp[i]==next3):
        i3 +=1
        next3 = dp[i3]*3
    if(dp[i]==next5):
        i5 +=1
        next5 = dp[i5]*5
print(dp[n-1])
