# 역시 못풀었다.ㅠ진짜 이 파트는 나중에 꼭 많이 풀어봐야겠다,,
# expandList로 확장 안시키고 키와 배열의 크기로만 푸는 방법

import copy
def rotation(key,m):
    rkey = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rkey[j][m-1-i] = key[i][j]
    return rkey

# 자물쇠가 key로 시도해봤을 때, 열리는지 테스트
def test(key,lock,i,j,m,n):
    # deepcopy를 위해 import copy를 해줘야 한다.
    # 그냥 dump = key 하면, shallow copy가 된다.
    dump = copy.deepcopy(lock)
    # lock 의 인덱스 
    for p in range(i,i+m):
        if 0<= p < n:
            for q in range(j,j+m):
                if 0<= q < n:
                    dump[p][q] += key[p-i][q-j] # key의 인덱스
    
    for line in dump:
        for item in line:
            if item !=1:
                return False
    return True
                
    
def solution(key, lock):
    m = len(key) # key
    n = len(lock) # lock
    # expandSize = (m-1)*2+n
    
    # lock은 고정, key가 움직인다.
    for _ in range(4):
        for i in range(-(m-1),n):
            for j in range(-(m-1),n):
                if test(key,lock,i,j,m,n):
                    return True
        key = rotation(key,m) 
    
    return False
    
# 배열을 확장해서 푸는 방법
def rotation(key):
    m = len(key)
    rkey = [[0]*m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            rkey[j][m-1-i] = key[i][j] 
            
    return rkey 

def test(key,lock,startX,startY,expandSize,start,end):
    expandList = [[0]*expandSize for _ in range(expandSize)]
    
    # expandList에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expandList[startX+i][startY+j] += key[i][j]
    
    # expandList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start,end):
        for j in range(start,end):
            expandList[i][j] += lock[i-start][j-start]
            if expandList[i][j] !=1:
                return False
    return True

def solution(key, lock):
    m = len(key)  # key
    n = len(lock) # lock
    expandSize = n+(m-1)*2
    
    start = m-1 # expandList에서 lock의 시작 지점
    end = start + n # expandList에서 lock이 끝나는 지점
    
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if test(key,lock,i,j,expandSize,start,end):
                    return True   
        key = rotation(key)
    
    return False
