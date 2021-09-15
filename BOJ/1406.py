import sys
input = sys.stdin.readline

str = list(input().rstrip())
cursor = len(str)
m = int(input())
for _ in range(m):
    cmd = input().rstrip()
    if 'P' in cmd:
        str.insert(cursor,cmd[-1])
        cursor += 1
    if 'L' in cmd:
        if cursor==0:
            continue
        else:
            cursor -= 1
    if 'D' in cmd:
        if cursor==len(str):
            continue
        else:
            cursor += 1
    if 'B' in cmd:
        if cursor==0:
            continue
        else:
            del str[cursor]
            cursor -= 1
print("".join(str))

# 시간초과 가 나서 질문검색에서 팁을 얻었다.
'''
이 문제를 제대로 풀기 위해서는 다음 중 한 가지를 선택해야 합니다.
python 의 list 는 연속된 메모리 공간을 할당해서 자료를 저장합니다.
list의 한가운데에 원소를 삽입하거나, 또는 한가운데 있는 원소를 삭제하기 위해서는 그 자리 이후의 원소들을 모두 한 칸씩 밀거나 당겨야 합니다.

1) list 의 맨 뒤에서만 삽입/삭제 연산을 할 수 있도록 알고리즘을 구현하기
2) 한가운데의 원소를 삽입하거나 삭제했을 때 바로 앞뒤의 원소 이외의 원소를 건드릴 필요가 없는 자료구조를 사용하기
'''
# 구글링을 참고한 풀이
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

str = list(input().rstrip())
m = int(input())
left = list(str)   
right = []

for _ in range(m):
    cmd = input().rstrip()
    if 'P' in cmd:
        left.append(cmd[-1])
    elif 'L' in cmd :
        if left:
            right.append(left.pop())
        else: 
            continue
    elif 'D' in cmd:
        if right:
            left.append(right.pop())
        else: 
            continue
    elif 'B' in cmd:
        if left:
            left.pop()
print("".join(left+right[::-1]))
'''
먼저 첫 번째 스택에 입력된 첫 문자열을 모두 담는다.
이때 커서 역할을 하는 것이 첫 번째 스택의 top이다.
커서를 왼쪽으로 움직이면 첫 번째 스택의 top을 pop한 뒤 이 결과를 두 번째 스택에 push하면 자연스럽게 커서가 왼쪽으로 움직인 효과를 낼 수 있다.
반대로 커서를 오른쪽으로 움직이면 다시 두 번째 스택의 top을 첫 번째 스택에 push 해주면 된다.
따라서 첫 번째 스택이 빈다면 커서가 문자열의 맨 왼쪽에 위치한 것이고, 두 번쨰 스택이 빈다면 커서가 문자열의 맨 오른쪽에 위치한 것이다.
문자를 추가하는 'P' 연산 역시 첫 번째 스택에 추가할 문자를 push해 주면 된다.'''

