# 내가 처음 푼 방법에서는 반례가 발견되었다. 
'''
먼저 풀었던 로직
1) 카드덱을 오름차순으로 정렬한다.
2) 2개씩 묶어서 쭉쭉 더한다.
반례 1)
    3 3 4 5
    => (3 + 3) = 6
    => (6 + 4) = 10
    => (10 + 5) = 15  
    최종 : 6 + 10 + 15 = 31

    => (3 + 3) = 6
    => (4 + 5) = 9
    => (6 + 9) = 15
    최종 : 6 + 9 + 15 = 30 => 얘가 더 최소값
반례 2)
    3 3 3 3
    => (3+3) = 6
    => (6+3) = 9
    => (9+3) = 12
    최종 : 6 + 9 + 12 = 27

    => (3+3) = 6
    => (3+3) = 6
    => (6+6) = 12
    최종 : 6 + 6 + 12 = 24 => 얘가 더 최소값

이러한 반례들이 너무 많이 존재하기 때문에, 최소값부터 더하면 안된다!
너무 단순했던 생각이기에 아닐 것을 알았다..방법이 안떠올랐다.

'''
# 질문검색을 참고해서 리스트로 풀었는데, 시간초과가 났다.
import sys
input = sys.stdin.readline

n = int(input())
card_list = []
for _ in range(n):
    card_list.append(int(input()))
card_list = sorted(card_list)
answer = 0

if(len(card_list)==1):
    print(0)
else:
    answer = 0
    while len(card_list) >1 : # 1개 일경우는 비교 안해도 된다.
        one = card_list.pop(0)
        two = card_list.pop(0)
        answer += one+two
        card_list.append(one+two) 
        card_list = sorted(card_list) 
    print(answer)

# <알게 된 사실> 
# 덱을 사용하려는데, 덱을 정렬하는 방법이 마땅히 없어, 우선순위 큐로 풀어야 했다. 우선순위 큐는 그 자체로 min_heap 구조이기 때문에, 정렬이 되어있다.
# 1) 덱만 잘 활용하면 큐는 사용하지 않아도 되는 줄 알았는데, 이러한 정렬을 최신화해야 하는 문제에서는 힙큐말고는 마땅한 자료구조가 없더라..
# (덱을 sorted 하면 type이 리스트로 바뀐다.)
# 2) pop(0)을 하는 것은 시간적으로 많은 비용을 발생시킨다. 다른 원소들을 앞으로 다 땡기기 때문에, 또한 사용할때도 주의해야 하므로, 이럴땐 덱을 사용하자.
'''
test1 = [0, 0, 0, 1, 2, 3, 4, 5, 6]  
for _dummy in test1:
    if(_dummy == 0):
        test1.pop(0)
        print(test1)

[0, 0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]

출력값 : [0, 1, 2, 3, 4, 5, 6]
인덱스도 고려해줘야 하므로, 의도했던바와는 다르게 오류가 발생할 여지가 있다. 지양하자.
'''
# 3) append의 리턴값도 sort()와 같이 None 이더라
'''
card_list = card_list.append(something)
과 같이 코드를 작성하면, card_list에 None 이 할당되기 때문에, 더 이상의 진행에 오류가 발생한다.
append는 그냥 
card_list.append(something) 과 같이 append문 자체만 써주자.
'''

# 우선순위 큐를 이용한 최종 코드 ( 1068ms)
from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
card_list = PriorityQueue()
answer = 0 
for _ in range(n):
    card_list.put(int(input()))

while card_list.qsize() >=2:
    one = card_list.get()
    two = card_list.get()
    answer += one+two
    card_list.put(one+two)

print(answer)

# 힙큐를 이용한 최종 코드 --> 가장 빨랐다.(252ms)
import heapq
import sys
input = sys.stdin.readline
n = int(input())
card_list = []
answer = 0 
for _ in range(n):
    heapq.heappush(card_list,int(input()))

while len(card_list) >=2:
    one = heapq.heappop(card_list)
    two = heapq.heappop(card_list)
    answer += one+two
    heapq.heappush(card_list,one+two)

print(answer)
