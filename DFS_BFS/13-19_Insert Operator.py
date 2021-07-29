# 일단 30분안에는 못 풀었다. 처음에는 백준에서 시간초과가 나서 PyPy로 돌렸는데, 통과됐다.
# 백준 질문 검색란에 반례를 찾다가 다시 코드를 고쳤는데, permutaiton할 때, 중복제거를 하면 연산자 리스트 길이를 줄일 수 있다는 힌트를 얻었다.
# set()만 해줬는데도 파이썬3가 통과되었다.
# 최종코드는 아래와 같은데, 시간은 통과되었지만, 메모리를 너무 잡아먹었고 dfs,bfs로 풀기보다는 순열을 import 해서 풀어버렸다,,

import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

n = int(input())  # 숫자 개수 입력받기
number_list= list((map(int,input().split())))  # 숫자 입력받기
operator = list(map(int,input().split()))  # 연산자 개수 차례로 입력받기
real_operator = deque([])  # 연산자 리스트
for idx,x in enumerate(operator):    # 연산자 개수 리스트 돌면서 
    if(idx==0):  # 인덱스가 0이면 더하기 
        real_operator.append('+'*x)
    if(idx==1):  # 인덱스가 1이면 빼기 
        real_operator.append('-'*x)
    if(idx==2):  # 인덱스가 2이면 곱하기 
        real_operator.append('x'*x)
    if(idx==3):  # 인덱스가 3이면 나누기 
        real_operator.append('/'*x)
real_operator = "".join(real_operator)  # [3,1,0,4] 라면 앞선 단계에서 ['+++','-','','////'] 이니까 문자열로 바꿔주고 
real_operator = list(real_operator)  # 다시 각각 리스트화 시켜준다. --> ['+','+','+','-','/','/','/','/'] 가 된다.

# 각 리스트를 순열 돌리면서 문자열 리스트를 만들어준다. 
real_operator = list((set(list(map(''.join,permutations(real_operator))))))  # 여기서 중간에 set을 안해주면, 시간초과가 났다!
                                                                             # (순열에서는 각기 다른 위치는 다른 것으로 인식하기 때문에 연산자 리스트 중복이 일어난다.(중복제거해준다.))
# 최대, 최소 초기값 설정
max_sum = float("-inf")
min_sum = float("inf")

# 연산자 문자열 리스트 돌면서 
for operators in real_operator:
    sum = number_list[0] # number_list의 처음값이 일단 sum의 초기값
    for idx,o in enumerate(operators): # enumerate를 통해 idx인식하게 한다.
        if o == "+":   
            sum +=number_list[idx+1]  # number_list의 인덱스가 operator의 인덱스보다 1많으니까 number_list[idx+1] 값을 계산해준다.
        elif o == "-":
            sum -=number_list[idx+1]
        elif o == "x":
            sum *=number_list[idx+1]
        elif o == "/":
            if(sum>=0): 
                sum //=number_list[idx+1]
            else:  # 음수면,
                sum = -sum  # 양수로 바꿔주고
                (sum) //= number_list[idx+1]  # 몫나눗셈 해주고 
                sum = -sum  # 다시 음수로 바꿔준다.
    if(sum>max_sum):
        max_sum = sum
    if(sum<min_sum):
        min_sum = sum

print(max_sum)
print(min_sum)
#################################################################################################################################################################
# 답지 풀이
# 순열 permutation 말고 중복순열 클래스인 product 클래스를 사용하면 따로 set을 안해줘도 된다.
# 쓰는 방법 -> from itertools import product
# n = 4
# print(list(product(['+','-','*','/'],repeat = (n-1)))) --> n-1= 3개씩 뽑아서 중복순열
# [('+', '+', '+'), ('+', '+', '-'), ('+', '+', '*'), ('+', '+', '/'), ('+', '-', '+'), ('+', '-', '-'), ('+', '-', '*'), ('+', '-', '/'), 
# ('+', '*', '+'), ('+', '*', '-'), ('+', '*', '*'), ('+', '*', '/'), ('+', '/', '+'), ('+', '/', '-'), ('+', '/', '*'), ('+', '/', '/'), 
# ('-', '+', '+'), ('-', '+', '-'), ('-', '+', '*'), ('-', '+', '/'), ('-', '-', '+'), ('-', '-', '-'), ('-', '-', '*'), ('-', '-', '/'), 
# ('-', '*', '+'), ('-', '*', '-'), ('-', '*', '*'), ('-', '*', '/'), ('-', '/', '+'), ('-', '/', '-'), ('-', '/', '*'), ('-', '/', '/'), 
# ('*', '+', '+'), ('*', '+', '-'), ('*', '+', '*'), ('*', '+', '/'), ('*', '-', '+'), ('*', '-', '-'), ('*', '-', '*'), ('*', '-', '/'), 
# ('*', '*', '+'), ('*', '*', '-'), ('*', '*', '*'), ('*', '*', '/'), ('*', '/', '+'), ('*', '/', '-'), ('*', '/', '*'), ('*', '/', '/'), 
# ('/', '+', '+'), ('/', '+', '-'), ('/', '+', '*'), ('/', '+', '/'), ('/', '-', '+'), ('/', '-', '-'), ('/', '-', '*'), ('/', '-', '/'), 
# ('/', '*', '+'), ('/', '*', '-'), ('/', '*', '*'), ('/', '*', '/'), ('/', '/', '+'), ('/', '/', '-'), ('/', '/', '*'), ('/', '/', '/')] 이런식으로 나온다.

# dfs 풀이--- 순열보다 속도가 10배는 빨랐다.(148ms)
import sys
from collections import deque
# import copy
from itertools import permutations
input = sys.stdin.readline

n = int(input())
number_list= list((map(int,input().split())))
add,sub,mul,div = map(int,input().split())

# 최댓값 최솟값 초기화
max_value = -1e9
min_value = 1e9

# 깊이 우선 탐색 메서드

def dfs(i,now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n :
        min_value = min(min_value,now)
        max_value = max(max_value,now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0 :
            add-=1
            dfs(i+1, now+number_list[i])
            add+=1
        if sub > 0 :
            sub-=1
            dfs(i+1, now-number_list[i])
            sub+=1
        if mul > 0 :
            mul-=1
            dfs(i+1, now*number_list[i])
            mul+=1
        if div > 0 :
            div-=1
            dfs(i+1, int(now/number_list[i])) # 나눌때는 나머지를 제거
            div+=1

dfs(1,number_list[0]) # 현재 number_list 0번째 값부터 시작하고 1번째 number_list부터 보면 된다.

print(max_value)
print(min_value)
