# 테스트 케이스는 통과되었지만, 백준 돌리니까 실패
# 합쳐진 국가의 가장자리 인덱스 구하다가 지쳐서 포기 --> 거기서부터해야 반례도 해결가능
'''
4 1 9
96 93 74 30
60 90 65 96
5 27 17 98
10 41 46 20
correct: 1

(96,93,90)->93
(74,65)->69
(96,98)->97
(5,10)->7
(41,46)->43

/************/
5 1 5
88 27 34 84 9
40 91 11 30 81
2 88 65 26 75
75 66 16 14 28
89 10 5 30 75
correct: 1

(91,88)->89
(30,26)->28
(16,14)->15
(10,5)->7

2 10 20
0 30
50 10

2 10 20 
0 20
50 20

2 10 20
10 10
50 20

2 10 20
10 15
50 15

answer : 3
'''

import sys
from collections import deque
import copy
from itertools import combinations, permutations
input = sys.stdin.readline

def take_a_look(x,y,population,country):
    for d in range(4):
        nx = x+dr[d]
        ny = y+dc[d]
        if(0<=nx<N and 0<=ny<N):
            if(L<=abs(population-ground[nx][ny])<=R):
                # if(changed[nx][ny]==False):
                country[nx][ny]=country[x][y]
                    # changed[nx][ny]=Tru
    return country

def day_count(country):
    alive_country = []
    position = []
    for i in range(N):
        for j in range(N):
            alive_country.append(country[i][j])
    alive_country = list(set(alive_country))
    # country_count = len(alive_country)
    for c in alive_country:
        cal = 0
        total_pop = 0  
        for x in range(N):
            for y in range(N):
                if(country[x][y]==c):
                    cal +=1
                    total_pop+=ground[x][y]
                    position.append([x,y])
        renewal = total_pop // cal
        while(len(position)!=0):
            rx,ry = position.pop()
            ground[rx][ry] = renewal
    return ground

def process(ground,country):
    countryB = copy.deepcopy(country)
    for x in range(N):
        for y in range(N):
            if(hoxy(x,y,countryB)):
                population = ground[x][y]
                country = take_a_look(x,y,population,country)   
            else:
                continue
    
    print(country)

    ground = day_count(country)
    return ground, country


day = 0
N,L,R = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
# L <= x <= R
country = []
num = 0 

# 각 (행,렬)마다 국가번호 지정 (0~N-1)
for i in range(N):
    line = []
    for j in range(N):
        line.append(num)
        num+=1
    country.append(line)
# print(visited)
dr = [-1,1,0,0] # 상 하 좌 우
dc = [0,0,-1,1] # 상 하 좌 우

changed=[[False for _ in range(N)] for _ in range(N)]
# print(changed)
# territory = []
while True:
    countryA = copy.deepcopy(country)
    ground, country = process(ground,country)
    if(countryA!=country):
        day+=1
    else:
        break
print(day)
