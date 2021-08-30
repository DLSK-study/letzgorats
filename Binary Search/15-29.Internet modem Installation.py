# 내가 푼 방법 -- 반례를 못 찾겠다.. 백준은 틀렸다고 나온다 계속,,
import sys
input = sys.stdin.readline

def find_house(start,end,house_list,c):
    global answer
    c-=2
    while c > 0 :
        mid = (start+end) // 2
        tmp = house_list[mid]
        if(tmp-house_list[start] < house_list[end]-tmp):
            answer = tmp-house_list[start]
            start = mid
            c -= 1
        elif(tmp-house_list[start] > house_list[end]-tmp):
            answer = house_list[end]-tmp
            end = mid
            c -= 1
        else:
            left = mid-1
            right = mid+1
            while tmp - house_list[left] == house_list[right] -tmp:
                left-=1
                right+=1
                if left == start:
                    answer = tmp - house_list[start]
                    start = mid
                    c -= 1
                    break
                elif right == end:
                    answer = house_list[end]-tmp
                    end = mid
                    c -= 1
                    break
            if(tmp - house_list[left] > house_list[right] -tmp):
                answer = house_list[end]-tmp
                end = mid
                c -= 1
            elif(tmp - house_list[left] < house_list[right] -tmp):
                answer = tmp - house_list[start]
                start = mid
                c -= 1

n,c = map(int,input().split())
house_list = []
house_list = sorted(int(input()) for _ in range(n))
answer = max(house_list)-min(house_list)
find_house(0,n-1,house_list,c)
print(answer)

# 답지 풀이
import sys
input = sys.stdin.readline

n,c = map(int,input().split())
house_list = []
house_list = sorted(int(input()) for _ in range(n))

start = 1 # 가능한 최소 거리(min gap)
end = house_list[-1] - house_list[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start+end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = house_list[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치
    for i in range(1,n): # 앞에서부터 차근차근 설치
        if house_list[i] >= value + mid:
            value = house_list[i]
            count+=1
    if count >= c : # c개 이상의 공유기를 설치하는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리르 감소
        end = mid - 1

print(result)
