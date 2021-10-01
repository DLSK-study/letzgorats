# 시간초과가 났다..pypy3로도..
import sys
input = sys.stdin.readline

n = int(input())
answer = 0

def promising(i,col):
    k = 1
    flag = True
    while(k<i and flag):
        # 같은 열에 있는지 혹은 같은 대각선에 있는지 판단
        if(col[i] == col[k] or abs(col[i]-col[k])==(i-k)):
            flag = False
        k+=1
    return flag

def n_queens(i,col):
    global answer 
    n = len(col) - 1
    if(promising(i,col)):  # 유망한지 판단
        if i == n :   # i == n 이면, 가지치기 끝까지 내려온 것, 즉 경우의 수가 하나 생겼다는 뜻
            # print(col[i:n+1])
            answer+=1
        else:   # 그렇지 않으면
            for j in range(1,n+1):
                col[i+1] = j    # 다시 col[i+1]을 j로 설정하고 
                n_queens(i+1,col)  # 재귀적 탐색


col = [0]*(n+1)
n_queens(0,col)
print(answer)

# 풀이 출처 : https://www.youtube.com/watch?v=z4wKvYdd6wM
