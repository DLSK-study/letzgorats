# 20분안에 못 풀었다.
 
# 맨 처음 푼 코드 -- 답은 나왔는데, 시간초과 였다.
import sys
input = sys.stdin.readline

n = int(input())
house=sorted(list(map(int,input().split())))
possible = {}

for standard in house:
    sum = 0 
    for h in house:
        sum+=abs(h-standard)
    possible[standard]=sum

possible = sorted(possible.items(),key = lambda x :x[1]) # 거리기준으로 정렬
print(possible[0][0]) # 그 중에서 가장 집값의 위치가 작은 값을 출력

# 두 번째로 고친 코드 - set으로 중복제거 해줌으로써 오류를 잡았고, 데이터 개수 줄였다.-- 하지만 여전히 시간초과
import sys
input = sys.stdin.readline

n = int(input())
house=sorted(list(set((map(int,input().split())))))

min_value =  float('inf')
for i in house:
    sum = 0
    for j in house:
        sum += abs(j-i)
    if(min_value > sum):    # 크거나 같은 것을 안해줬기 때문에 if문에 들어가게 된다면 가장 작은값은 i 이다.
        min_value = sum
        answer = i

print(answer)

## 여기까지 했는데, 20분 초과되었다.
## 수학적으로 생각하면, 결국 가운데 값이 가장 거리가 최소다.
import sys
input = sys.stdin.readline

n = int(input())
house=sorted(list(set((map(int,input().split())))))

print(house[(len(house)-1)//2]) # 여전히 틀렸다고 나왔다. 이유가 뭔지 모르겠다.

# 최종 코드
import sys
input = sys.stdin.readline

n = int(input())
house=sorted(list(map(int,input().split())))  # set을 없애주니까 맞았다고 나왔다.

print(house[(n-1)//2])

''' 반례 
3 
1 10 10
이면, 1 이 나와야 하지 않나? 10이 나오는데 왜 맞을까,,?
'''
