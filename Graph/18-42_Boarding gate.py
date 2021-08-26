# 테스트케이스는 통과하지만, 시간제한이 1초이고 메모리가 10만이기 때문에, 효율적으로 풀어야 한다.
# 내가 푼 방법
import sys
input = sys.stdin.readline

gate = int(input())
plane = int(input())

possible_docking = [0] * (gate+2)
plane_docking = []
for i in range(plane):
    plane_docking.append(int(input()))
print(plane_docking)
count = 0
onlyone = False

for plane_num,until_gate in enumerate(plane_docking):
    print(plane_num,"plane_num")
    print(until_gate,"until_gate")
    possible = False
    for num in range(1,until_gate+1):
        if possible_docking[num] == 0:
            possible_docking[num] = 1
            count+=1
            possible = True
            break
        if onlyone==False and until_gate == 1 : # 1번 게이트에 도킹할 수 있는 입력은 한번만 나오는 것만 가능
            count +=1
            onlyone = True
    if possible == False :
        break
print(count)


# 그래프로 푸는 방법
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b 
        

gate = int(input())
plane = int(input())

parent = [0] *(gate+1)

for i in range(1,gate+1):
    parent[i] = i

result = 0 
docking_gate = []
for _ in range(plane):
    docking_gate.append(int(input()))

for d in docking_gate:
    d = find_parent(parent,d) # 현재 비행기의 탑승구의 루트 확인
    if d== 0:
        break
    else:
        union_parent(parent,d,d-1) # 그렇지 않으면, 바로 왼쪽의 집합과 합치기
        result += 1

print(result)
