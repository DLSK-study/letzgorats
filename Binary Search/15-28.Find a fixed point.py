# answer의 초기값을 -1로 잡고 그냥 바로 입력한 수와 입력한 인덱스 순서가 같으면 answer을 해당 수로 바꿔주는 방법
import sys
input = sys.stdin.readline

n = int(input())
answer = -1
for idx,i in enumerate(input().split()):
    if idx == int(i) :
        answer = i
print(answer)


# 계수 정렬로 푼 방법
import sys
input = sys.stdin.readline

n = int(input())
count_list = [0] * 1000001
point = False
for idx,i in enumerate(input().split()):  # 입력을 순서대로 받되, enumerate로 idx도 순회한다.
    if idx == int(i) :   # 입력받은 순서가 곧 리스트의 순서이므로 idx 가 int(i)와 같다면
        count_list[int(i)] = 1   # count_list의 해당 인덱스를 1로 바꿔준다
        point = True  # point는 True가 된다.
if point == True: # point 가 True 면 고정점이 있다는 뜻이므로
    print(count_list.index(1))  # count_list에 있는 1의 인덱스를 출력
else:  # 그렇지 않으면
    print(-1)  # -1 출력

    
# 답지 풀이 -- 이진 탐색 풀이
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array,start,end):
    if start > end :
        return None
    mid = (start + end ) //2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid :
        return binary_search(array,start,mid-1)
    else:
        return binary_search(array,mid+1,end)
        
n = int(input())
array = list(map(int,input().split()))

# 이진 탐색 수행
index = binary_search(array,0,n-1)

if index == None:  # 고정점이 없는 경우
    print(-1)
else:  # 고정점이 있는 경우
    print(index)
