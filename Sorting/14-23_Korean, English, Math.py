import sys
input = sys.stdin.readline

n = int(input())
info = []
for i in range(n):
    name,korean,english,math = input().split()
    info.append([name,int(korean),int(english),int(math)]) # [이름,국어점수,영어점수,수학점수] 리스트를 info 리스트에 입력받은대로 넣는다.
info = sorted(info, key= lambda x : (-x[1],x[2],-x[3],x[0])) # 기준 여러개를 동시에 정렬하는 방법, 문제에서 주어진 우선순위 순서대로 정렬한다. 

for i in info:
    print(i[0])
