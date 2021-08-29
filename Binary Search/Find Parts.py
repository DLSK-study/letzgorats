# 내가 푼 방법 -- 이진 탐색 (반복문)
import sys
input = sys.stdin.readline

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] < target :
            start = mid + 1
        elif array[mid] > target :
            end = mid - 1
        else:
            return mid
    return None

n = int(input())
product_list = list(map(int,input().split()))
m = int(input())
wanna_get = list(map(int,input().split()))

for x in wanna_get:
    answer = binary_search(product_list,x,0,n-1)
    if answer == None:
        print("no",end =" ")
    else:
        print("yes",end= " ")
        
# 답지 보니까 계수정렬이랑 집합 자료형을 이용했다고 해서 그 방법으로도 풀고자 했다.
# 계수 정렬로 푸는 방법
import sys
input = sys.stdin.readline

n = int(input())
count_list = [0] * 1000001
for i in input().split():  # 따로 product_list를 만드는 것이 아니라 입력 받은 값을 그대로 count_list 에 추가
    count_list[int(i)] += 1
m = int(input())
wanna_get = list(map(int,input().split()))

for i in wanna_get:
    if count_list[i] > 0 :
        print("yes",end=" ")
    else:
        print("no",end=" ")

# 집합 자료형으로 푸는 방법
import sys
input = sys.stdin.readline

n = int(input())
product_list = set(map(int,input().split()))
m = int(input())
wanna_get = list(map(int,input().split()))

for i in wanna_get:
    if i in product_list:
        print("yes",end=" ")
    else:
        print("no",end=" ")
