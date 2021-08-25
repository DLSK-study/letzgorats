**최단 경로(Shortest Path) 란 ?**

**: 말 그대로 가장 짧은 경로를 찾는 알고리즘**이다. **'길 찾기' 문제**라고도 불리는데, 다양한 유형이 있다. 예를 들어, "한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우" 나 "모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우" 등이 있다. 보통, 최단 경로 문제는 그래프를 이용해 표현하는데, 각 **지점은 그래프에서 '노드(node)'로 표현되고, 각 지점마다 연결된 도로는 그래프에서 '간선(edge)'으로 표현**된다. 코딩 테스트에서는 보통 최단 경로를 모두 출력하는 문제보다는 '최단 거리'를 출력하는 문제가 많다.

학부 수준에서 다루는 최단 거리 알고리즘은 대표적으로 아래와 같다.

> 1. 다익스트라 알고리즘

    2. 플로이드 워셜

    3. 벨만 포드 알고리즘

이 중에서, 코딩 테스트에서는 다익스트라 최단 경로와 플로이드 워셜 알고리즘 유형이 가장 많이 등장하는 유형이다.

---

### **다익스트라 최단 경로 알고리즘**

: 다익스트라(Dijkstra) 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, **특정한 노드에서 출발**하여 **다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘**이다. 다익스트라 알고리즘에서는, "**간선이 모두 0 이상의 값을 가진다**"를 가정한다. 때문에, 실제로 GPS 소프트웨어의 기본 알고리즘으로 채택되곤 한다. 다익스트라 최단 경로 알고리즘은 기본적으로 그리디와 결을 같이 하는데, 매번 "가장 비용이 적은 노드"를 선택해서 임의의 과정을 반복하기 때문이다. 원리는 아래와 같다.

> ① 출발 노드 설정② 최단 거리 테이블 초기화③ 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택④ 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신⑤ 위 과정에서 3번,4번 반복

여기서, "각 노드에 대한 현재까지의 최단 거리" 정보를 항상 1차원 리스트에 저장하며, 리스트를 계속 갱신해나가는데, 이를 최단 거리 테이블이라고도 부른다. 다익스트라 알고리즘을 구현하는 방법은 2가지이다.

> ① 구현하기는 쉽지만, 느리게 동작하는 코드                                                                         ② 구현하기는 까다로워도, 빠르게 동작하는 코드

당연히, ②번을 정확히 이해하고 구현할 수 있을 때까지 연습해야한다. 그래야 고난이도 문제를 만났을 때도 비교적 수월하게 풀 수 있다.

---

먼저, 다익스트라 알고리즘의 동작 원리를 살펴보자.

![https://blog.kakaocdn.net/dn/cbUu0v/btrb82zKpKy/XrUzHHHWzrU5d4c7xZppQ1/img.png](https://blog.kakaocdn.net/dn/cbUu0v/btrb82zKpKy/XrUzHHHWzrU5d4c7xZppQ1/img.png)

![https://blog.kakaocdn.net/dn/djxhWs/btrb6sMDgz8/wKkZzOYkLYuYNeGYhVDMp1/img.png](https://blog.kakaocdn.net/dn/djxhWs/btrb6sMDgz8/wKkZzOYkLYuYNeGYhVDMp1/img.png)

먼저, ①번의 간단한 다익스트라 알고리즘의 시간복잡도는 **O(V^2)** 를 가진다. 여기서, **V는 노드의 개수**를 의미한다. 이 알고리즘은 직관적이고 쉽게 이해가능하다. 처음에 각 노드에 대한 **최단 거리를 담는 1차원 리스트를 선언**하고, 이후에 단계마다 "방문하지 않은 노드중에서 **최단 거리가 가장 짧은 노드를 선택"하기 위해 매 단계마다 1차원 리스트의 모든 원소를 탐색**한다. 

사실 완벽한, 최단 경로를 구하려면 모든 경로를 출력할 줄 알아야 하는데, 대부분의 코딩테스트에서는 **특정한 노드에서 다른 특정한 노드까지의 최단거리만을 출력하도록 요구**한다.

①번의 간단한 다익스트라 알고리즘을 코드로 구현한 것은 아래와 같다.

```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 의미

# 노드의 개수, 간선의 개수 입력 받기
n, edge = map(int,input().split())

# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] *(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] *(n+1)

# 모든 간선 정보를 입력받기
for _ in range(edge):
	a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get smallest_node():
	min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
    	if distance[i] < min_value and not visited[i]:
        	min_value = distance[i]
            index = i
    return index 

def dijkstra(start):
	# 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
    	distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
    	# 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    	now  = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]
        	cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
            	distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
	# 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
		print("INFINTIY")
    # 도달할 수 있는 경우 거리를 출력
    else:
    	print(distance[i])
```

코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 일반적으로 위 코드로 풀 수 있을 것이지만, 노드의 개수가 10000개가 넘어가면, 시간 복잡도가 **O(V^2)** 라서, 개선된 알고리즘을을 이용해야 할 것이다.

---

②번의 개선된 다익스트라 알고리즘의 시간복잡도는 **O(ElogV)** 를 보장한다. 여기서, **V는 노드의 개수**를 의미하고, **E는 간선의 개수**를 의미한다. ①번 알고리즘에서 최단 거리가 가장 짧은 노드를 찾는 과정을 선형적으로 탐색하지 않고, **힙 자료구조를 사용**하게 되면 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로 복잡도를 확 줄일 수 있다. 먼저, 힙 구조에 대해 간단히 살펴보자.

힙 자료구조는 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나이다. 우선순위 큐는 우선순위가 가장 높은 데이터를 먼저 삭제한다는 점이 특징이다. 코딩 테스트에서도 자주 활용되는 자료구조 중 하나인데, 보통 PriorityQueue 나 heapq 라이브러리를 사용한다. 이 중에서도 heapq가 더 수행시간이 빠르기 때문에, **heapq를 사용하는 것이 적합**하다. 보통 (a,b)로 묶어서 우선순위 큐 자료구조에 넣는다면, 꺼낼 때는 a 를 기준으로 우선순위가 결정된다. 또한, 우선순위 큐를 구현할 때는 내부적으로 min heap(최소 힙)이나 max heap(최대 힙)을 이용하고, 파이썬 기본 라이브러리에서는 **min heap**이 디폴트이다. **다익스트라 최단 경로 알고리즘**에서도 이를 그대로 사용하는 것이 적절하다. 최대 힙을 사용하는 것에 대해서는 이 링크에서 자세히 설명하겠다.

구현하는 방법은, 단순히 우선순위 큐를 이용해서 시작 노드로부터 **'거리가 짧은 노드' 순서대로 큐에서 나올 수 있도록 작성**하면 된다. 우선순위 큐를 적용하여도 다익스트라 알고리즘이 동작하는 기본 원리는 동일하고, **최단 거리를 저장하기 위한 1차원 리스트(최단 거리 테이블)도 ①번과 같이 그대로 이용하되**, **현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용**한다고 보면 된다. 동작 원리를 살펴보자.

![https://blog.kakaocdn.net/dn/GqizP/btrb9QeUtgN/xlkajh3biKsxktN4ayZiK0/img.png](https://blog.kakaocdn.net/dn/GqizP/btrb9QeUtgN/xlkajh3biKsxktN4ayZiK0/img.png)

![https://blog.kakaocdn.net/dn/tLXhE/btrclINnUCs/riPY1KYJdZ5EgLU1ob82n0/img.png](https://blog.kakaocdn.net/dn/tLXhE/btrclINnUCs/riPY1KYJdZ5EgLU1ob82n0/img.png)

마지막으로, 최단 거리 테이블에 남은 0,2,4,1,2,3,5가 각 노드로의 최단 거리이다. 파이썬에서 제공하는 PriorityQueue와 heapq는 데이터의 개수가 N개일 때, 하나의 데이터를 삽입 및 삭제할 때의 시간 복잡도가 O(logN)이다. 앞선 코드와 비교해본다면, get_smallest_node() 라는 함수를 작성할 필요가 없다는 특징이 있다. "**최단 거리가 가장 짧은 노드를 선택"하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체 할 수 있기 때문**이다.

②번의 개선된 다익스트라 알고리즘을 코드로 구현한 것은 아래와 같다.

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, edge = map(int,input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ i in range(edge):
	a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    	graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q : # 큐가 비어있지 않다면
    	# 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면, 무시
        if distance[now] < dist :
        	continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
        	cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            	if cost < distance[i[0]]:
            		distance[i[0]] = cost
                	heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
	# 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF : 
    	print("INFINITY")
	# 도달할 수 있는 경우 거리를 출력
    else:
    	print(distance[i])
```

위의 코드처럼, 개선된 다익스트라 알고리즘의 시간복잡도는 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사하다고 볼 수 있다. 간단히 말해, 최대 E개의 간선 데이터를 힙에 넣었다가 다시 빼는 것으로 볼 수 있으므로 O(ElogE)임을 이해할 수 있겠다. 이 때, 중복 간선을 포함하지 않는 경우, E는 항상 V^2보다 작다. 왜냐하면, 모든 노드끼리 서로 다 연결되어 있다고 하면, 간선의 개수를 약 V^2로 볼 수 있고, E는 항상 V^2이하이기 때문이다. logE는 logV^2보다 작으므로 O(logV^2)는 O(2logV)=O(logV)가 되겠고, 다익스트라 알고리즘의 **전체 시간 복잡도는 O(ElogV)**가 되겠다. 위의 우선순위 큐를 필요로 하는 코드를 잘 이해한다면, 그래프 문제로 유명한 최소 신장 트리 문제를 풀 때도, **Prim 알고리즘의 구현이 다익스트라 알고리즘 구현과 흡사**하기 때문에 이해하기 수월할 것이다. 꼭 익숙해지자.

---

### **플로이드 워셜 알고리즘**

: 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우인 다익스트라 알고리즘과는 다르게 **플로이드 워셜 알고리즘**은 **모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우**에 사용할 수 있는 알고리즘이다. 플로이드 워셜 알고리즘도 다익스트라와 비슷하게 "거쳐 가는 노드"를 기준으로 알고리즘을 수행하지만, 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요는 없다. 또한, 플로이드 워셜 알고리즘은 출발 노드가 1개인 것이 아니라 모**든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보를 담기 때문에, 2차원 리스트에 '최단 거리'정보를 저장**한다. 다익스트라가 그리디 알고리즘이라면, 플로이드 워셜 알고리즘은 **다이나믹 프로그래밍** 이라고 할 수 있다. 노드의 개수가 N이라면, N번만큼의 단계를 반복해, **점화식에 따라서 2차원 리스트를 갱신**하기 때문이다. 알고리즘의 원리는 현재 확인하고 있는 노드를 제외하고, N-1 개의 노드 중에서 서로 다른 노드 (a,b) 쌍을 선택한 후, 비용을 확인한 뒤에 최단 거리를 갱신한다. 즉, n-1P2 개의 쌍을 단계마다 반복해서 확인하면 된다는 뜻이다. 구체적인 (K번의 단계에 대한) 점화식은 아래와 같다.

> 

![https://blog.kakaocdn.net/dn/bMzZLz/btrcb9SWWmD/gYZBghQBNiKgPWBSYqQaj0/img.png](https://blog.kakaocdn.net/dn/bMzZLz/btrcb9SWWmD/gYZBghQBNiKgPWBSYqQaj0/img.png)

따라서, 전체적으로 3중 반복문을 통해 점화식에 맞춰 최단거리 테이블을 갱신하면 된다. 위의 점화식이 의미하는 내용을 말로 풀어 설명하자면, "A에서 B로 가는 촤소 비용"과 "A에서 K를 거쳐 B로 가는 비용" 중 더 작은 값으로 갱신하겠다는 의미다. 구체적으로 원리를 살펴보자.

![https://blog.kakaocdn.net/dn/9Dsyn/btrb663PoNB/0cvet9t4YcrY2EUVfl3OZ1/img.png](https://blog.kakaocdn.net/dn/9Dsyn/btrb663PoNB/0cvet9t4YcrY2EUVfl3OZ1/img.png)

![https://blog.kakaocdn.net/dn/Doxtv/btrcf8seXbz/7HKCZbZETbLLdUelYYEaR0/img.png](https://blog.kakaocdn.net/dn/Doxtv/btrcf8seXbz/7HKCZbZETbLLdUelYYEaR0/img.png)

위 예에서 최종적으로 나온 테이블 형태가 모든 노드에서 모든 노드로 가는 최단 거리 정보를 표현한 것이다. 예를 들어, 1번 노드에서 3번 노드로 가는 최단거리는 8이다. 이러한 플로이드 워셜 알고리즘을 소스코드로 표현해보자면, 아래와 같다.

```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
edge = int(input())
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
	for b in range(1,n+1):
    		if(a==b):
        		graph[a][b] = 0
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(edge):
	# A에서 B로 가는 비용은 C라고 설정
    	a,b,c = map(int,input().split())
    	graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
	for a in range(1,n+1):
    	for b in range(1,n+1):
		    graph[a][b] = min(graph[a][b],grapg[a][k] + graph[k][b])
            
# 수행된 결과를 출력
for a in range(1,n+1):
	for b in range(1,n+1):
    	# 도달할 수 없는 경우, 무한(INFINITY)를 출력
    		if (graph[a][b]  == INF) :
        		print("INFINITY",end=" ")
        # 도달할 수 있는 경우, 거리를 출력
    		else:
       			print(graph[a][b],end=" ")
    print()
```

3중 for문을 쓰기 때문에 **전체 시간 복잡도는 O(N^3)** 라고 볼 수 있겠고, 모든 노드에서 다른 모든 노드까지의 최단 거리를 알 수 있는 특징이 있다.

이상으로, **다익스트라 최단경로 알고리즘**과 **플로이드 워셜 알고리즘**에 대해 공부해봤다.
