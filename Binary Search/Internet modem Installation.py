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
