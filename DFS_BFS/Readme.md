먼저, 꼭 필요한 자료구조의 기초에 대해 살펴보자.

**'탐색'이란** 많은 양의 **데이터 중에서 원하는 데이터를 찾는 과정** 으로 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룬다. 대표적인 **탐색 알고리즘으로 DFS와 BFS** 가 있는데, 이를 제대로 이해하려면, 먼저 스택과 큐에 대한 이해가 선수되어야 한다.

먼저, **스택(stack)**을 살펴보자. 스택은 양동이에 물체를 넣는다고 생각하면 된다. 이러한 구조를 선입 후출(First In Last Out) 또는 **후입 선출**(Last In First Out),**LIFO** 구조라고 한다. 구조를 그림으로 그려보면 아래와 같다.

![https://blog.kakaocdn.net/dn/5Tbgi/btrakSsS26u/Vs2z7UKTbqK8bBssS6cNgK/img.jpg](https://blog.kakaocdn.net/dn/5Tbgi/btrakSsS26u/Vs2z7UKTbqK8bBssS6cNgK/img.jpg)

이를 파이썬 코드로 표현한다면,

```python
stack = [] # 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(1) - 삽입(7) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(7)
stack.pop()

print(stack) # 최하단 원소부터 출력 : [5, 2, 1]
print(stack[::-1]) # 최상단 원소부터 출력 :  [1, 2, 5]
```

파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append()와 pop() 메서드를 이용하면, 스택 구조와 동일하게 동작한다. 이 때, append()는 리스트의 가장 뒤쪽에 데이터를 삽입하고 pop()은 리스트의 가장 뒤쪽의 원소를 꺼낸다.

---

다음은, **큐(queue)**를 살펴보자. 큐는 새치기가 없는 대기 줄이라고 생각하면 된다. 이러한 구조를 **선입 선출**(First In First Out) **FIFO** 구조라고 한다. 구조를 그림으로 그려보면 아래와 같다.

![https://blog.kakaocdn.net/dn/AXOfY/btranWA6Lxt/zMfQvAtVzbZbkzJ2nJgE30/img.jpg](https://blog.kakaocdn.net/dn/AXOfY/btranWA6Lxt/zMfQvAtVzbZbkzJ2nJgE30/img.jpg)

이를 파이썬 코드로 표현한다면,

```python
from collections import deque # 큐(Queue) 구현을 위해 덱 라이브러리 사용
queue = deque() # 삽입(5) - 삽입(7) - 삭제() - 삽입(3) - 삽입(8) - 삭제 - 삭제()
queue.append(5)
queue.append(7)
queue.popleft()  # deque에 있는 메서드 popleft() : 가장 왼쪽의 원소를 빼준다.
queue.append(3)
queue.append(8)
queue.popleft()
queue.popleft()
print(queue) # deque([8])
```

deque은 스택과 큐의 장점을 모두 채택한 것인데, 넣고 빼는 속도가 일반 리스트 자료형에 비해 효율적이고, popleft()나 rotate() 등의 메서드를 사용할 수 있어 편하다. deque 객체를 리스트 자료형으로 변환하고자 할 때는, list(queue) 처럼 리스트화 시켜주면 된다.

---

DFS와 BFS를 구현하려면, 재귀 함수도 이해하고 있어야 하는데, **재귀함수** 란 자기 자신을 다시 호출하는 함수이다. 이해를 쉽게 하기 위해서 친구한테 이렇게 말하는 상황을 생각하면 된다.

더보기

약간 뫼비우스의 띠와도 비슷하게 느껴진다. 또, 재귀함수는 프랙탈(Fractal)구조와 유사하다. 삼각형 안에 또 다른 삼각형이 무한이 존재하는 그림 말이다.

재귀함수를 이용하는 대표적인 예제로는 팩토리얼이 있다. 재귀함수의 장점으로는 코드를 우리가 흔히 아는 점화식을 그대로 옮기기 때문에, 가독성이 좋다는 점이다. 반면, 속도는 더 느릴 수 있다.

```python
# 반복적으로 구현한 n!
def factorial_iterative(n):    
		result = 1    # 1부터 n 까지의 수를 차례대로 곱하기    
		for i in range(1,n+1):        
			result *= i    
		return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):	
		if n<=1 :
	    return 1
    else:         # n! = n * (n-1)! 그대로 작성    	
			return factorial(n-1) * n

print('반복적으로 구현: ',factorial_iterative(5))  # 반복적으로 구현:  120
print('재귀적으로 구현: ',factorial_recursive(5))  # 재귀적으로 구현:  120
```

컴퓨터 내부에서 재귀함수의 수행은 스택 자료구조를 이용한다. 함수를 계속 호출했을 때, 가장 마지막에 호출한 함수가 먼저 수행을 끝내야, 그 다음에 그 앞의 함수가 종료되고, 쭉 가다가 마지막이 되서야 가장 처음에 호출되었던 함수가 종료되는 방식이다. 컴퓨터 구조 측면에서 보자면, 실제로 연속해서 호출되는 함수는 메인 메모리의 스택 구조에 적재되곤 한다. DFS가 이런 스택 자료구조를 활용하는 알고리즘의 대표적인 예이다.

**DFS**는 **Depth-First Search** 의 약자로, **깊이 우선 탐색** 이라고 부르며, 그래프에서 **깊은 부분을 우선적으로 탐색**하는 알고리즘이다. DFS를 알아보기 전에, 먼저 그래프(Graph)의 기본 구조를 알아보자면,

**그래프**는 **노드(Node)와 간선(Edge)로 구성**되어 있으며, 이 때, **노드를 정점(Vertex)**라고도 부른다. **그래프 탐색**이란, **하나의 노드를 시작으로 다수의 노드를 방문**하는 것을 말하고, 두 노드가 간선으로 연결되어 있다면, "두 노드는 인접하다" 라고 한다.

프로그래밍에서는 그래프가 크게

1) **인접 행렬**(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

2) **인접 리스트**(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식

이렇게 2가지 방식으로 표현되는데, 예시를 살펴보자.

![https://blog.kakaocdn.net/dn/mvDKk/btrakTZMAJC/NkGDYPXuxeSbKfZEXD5LG0/img.jpg](https://blog.kakaocdn.net/dn/mvDKk/btrakTZMAJC/NkGDYPXuxeSbKfZEXD5LG0/img.jpg)

왼쪽과 같은 그래프가 있다고 하면, 이를 행렬로 나타내면

[제목 없음](https://www.notion.so/9ce5d53bf35c49ee95cf81180b9edce0)

와 같이 나타낼 수 있다. 이 때, 자기 자신을 제외한 노드와 **연결되어 있지 않은 노드끼리는 무한의 비용(INF)** 이라고 가정한다. 이를 코드로 나타내면, 아래와 같다.

```
INF = float('inf') # 무한의 비용 선언# 2차원 리스트를 이용해 인접 행렬 표현graph = [[0,7,5],[7,0,INF],[5,INF,0]]print(graph)# [[0, 7, 5], [7, 0, inf], [5, inf, 0]]
```

인접 리스트 방식에서는 데이터를 어떻게 저장할까?

위 그래프를 인접리스트로 표현하자면, 아래와 같이 나타낼 수 있다.

![https://blog.kakaocdn.net/dn/6n9et/btraoalEgvx/7rL4kVbS4EK5RkrNeSBdD0/img.jpg](https://blog.kakaocdn.net/dn/6n9et/btraoalEgvx/7rL4kVbS4EK5RkrNeSBdD0/img.jpg)

**각각의 모든 노드에 연결된 노드들에 대한 정보를 차례대로 연결해서 저장**한다는 소리이다. 이를 코드로 나타내면, 아래와 같다.

```python
# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)] # 노드 0 에 연결된 노드 정보 저장(노드,간선)
graph[0].append((1,5))graph[0].append((2,7)) # 노드 1에 연결된 노드 정보 저장(노드,간선)
graph[1].append((0,5)) # 노드 2에 연결된 노드 정보 저장(노드,간선)
graph[2].append((0,7))print(graph) # [(1, 5), (2, 7)], [(0, 5)], [(0, 7)]]
```

**메모리 측면**에서 보자면, 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을 수록 메모리가 불필요하게 낭비될 수 있는 반면, **인접 리스트 방식**은 연결된 정보만을 저장하기 때문에, **메모리를 효율적으로 사용**한다.

**속도 측면**에서 보자면, 인접 리스트 방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다. **인접 행렬**은 graph[i][j] 로만 **바로 확인할 수 있는데**, 인접 리스트는 연결된 데이터를 하나씩 다 확인해야 하기 때문이다.

---

### **< DFS > ( 깊이 우선 탐색 )**

DFS는 스택 구조를 사용한다고 앞서 설명을 했다.

깊이 우선 탐색의 과정은 다음과 같다.

더보기

일반적으로, 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면, 번호가 낮은 순서부터 처리한다.

그림으로 그 과정을 짚어보자. <**DFS>**

![https://blog.kakaocdn.net/dn/R8LlM/btraoaFWo1l/9n6tmhDDoFAfOwjqegudYk/img.png](https://blog.kakaocdn.net/dn/R8LlM/btraoaFWo1l/9n6tmhDDoFAfOwjqegudYk/img.png)

위와 같은 과정을 코드로 나타내보면 아래와 같다.

```python
# DFS 메서드 정의
def dfs(graph, vertex, visited) :    # 현재 노드를 방물 처리
    visited[vertex] = True
    print(vertex,end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[vertex]:
         if not visited[i]:
             dfs(graph,i,visited )

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[],[2,6,8],[1,3,4],[2,4],[2,3],[7],[1,7],[5,6,8],[1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph,1,visited)   # 결과값 : 1 2 3 4 6 7 5 8
```

---

### **< BFS > ( 너비 우선 탐색 )**

BFS는 쉽게 말하면, 가까운 노드부터 탐색하는 알고리즘이다. DFS는 최대한 멀리 있는 노드를 우선적으로 탐색한다고 치면, BFS는 완전 그 반대라고 할 수 있다. BFS 구현에서는 큐 자료구조를 사용하는 것이 일반적이다. 인접한 노드를 반복적으로 큐에 넣고, 선입선출이기 때문에, 먼저 들어온 것은 먼저 나가게 되어 자연스럽게 가까운 노드부터 탐색을 진행하게 된다.

너비 우선 탐색의 과정은 다음과 같다.

더보기

마찬가지로, 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면, 번호가 낮은 순서부터 큐에 넣는다.

그림으로 그 과정을 짚어보자. **<BFS>**

![https://blog.kakaocdn.net/dn/sqZWP/btraprNYCz3/UV42E7dpGM2Nge8KcYmu3k/img.png](https://blog.kakaocdn.net/dn/sqZWP/btraprNYCz3/UV42E7dpGM2Nge8KcYmu3k/img.png)

위와 같은 과정을 코드로 나타내보면 아래와 같다.

```python
from collections import deque# BFS 메서드 정의
def bfs(graph, start, visited) :
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빈 상태가 될 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=" ")
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[],[2,6,8],[1,3,4],[2,4],[2,3],[7],[1,7],[5,6,8],[1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
bfs(graph,1,visited)    # 출력 결과 : 1 2 6 8 3 4 7 5
```

정리하자면, **DFS**의 동작원리는 **스택**이고, 구현 방법은 **재귀 함수를 이용**하는 것이고, **BFS**의 동작원리는 **큐**이고, 구현 방법은 **큐 자료구조를 이용**해야 한다.

코딩 테스트 중에 맵이나 체스판 같이 2차원 배열에서의 탐색 문제를 만나면, 이렇게 그래프 형태로 바꿔서 생각하면 풀이를 조금 더 쉽게 떠올릴 수 있을 것이다. 코딩 테스트에서 그래프 BFS/DFS 는 정말 잘 나오는 문제이기 때문에, 꼭 자료구조와 더불어 유형을 숙지해야 할 것이다!
