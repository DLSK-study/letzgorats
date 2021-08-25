'DFS/BFS'와 '최단 경로'에서 다룬 내용도 그래프 알고리즘의 한 유형으로 볼 수 있다. 그래프 알고리즘은 코딩 테스트에서 출제 비중이 낮은 편이지만, 출제되기 때문에 기타 그래프 알고리즘도 살펴볼 필요가 있다. 지금부터 다룰 알고리즘은 앞서 배운 내용에 기반하는데, 예를 들어 **크루스칼 알고리즘(Kruskal Algorithms)**은 **그리디 알고리즘으로 분류**되고, **위상 정렬 알고리즘(Topology Algorithms)**은 앞서 배운 **큐 자료구조 혹은 스택 자료구조를 활용**해야 구현할 수 있다. 복습을 해보자면, 그래프란 노드와 간선의 정보를 가지고 있는 자료구조이고, 알고리즘 문제에서 '서로 다른 개체가 연결되어 있다'는 얘기가 있다면 가장 먼저 그래프 알고리즘을 떠올려야 한다.

더불어, 그래프 자료구조 중에서 **트리(Tree)자료구조**는 다양한 알고리즘에서 사용되므로 반드시 기억해야 한다. 다익스트라 최단 경로 알고리즘에서 우선순위 큐가 사용되었는데, 이 우선순위 큐를 구현하기 위해서는 **최소힙(Min Heap)이나 최대힙(Max Heap)**을 이용해야 한다. 이 때, 최소힙은 항상 부모 노드가 자식노드보다 크기가 작은 자료구조로서 트리 자료구조에 속한다. 트리 자료구조와 그래프를 비교하자면 아래와 같다.

[제목 없음](https://www.notion.so/4608a1292d5542bdbe86d6d6a4920e68)

**그래프의 구현 방법**은 DFS/BFS 에서도 살펴봤다시피 2가지 방식이 존재한다.

> 인접 행렬 : 2차원 배열을 사용 -- 메모리 ↑/ 속도 더 빠름                                                       
> 인접 리스트 : 리스트를 사용 -- 메모리 ↓/ 속도 더 느림

두 방식은 **메모리와 속도 측면에서 구별**이 된다는 점을 숙지하자. V가 노드의 개수, E가 간선의 개수라고 할 때, 인접행렬은 O(V^2)만큼의 메모리 공간이 필요한 반면, 인접 리스트를 이용할 때는 간선의 개수만큼인 O(E)만큼의 메모리 공간이 필요하다. 또한, 인접 행렬은 특정한 노드에서 다른 노드로 이어지는 간선의 비용을 O(1)의 시간으로 즉시 알 수 있는 반면, 인접 리스트는 O(V) 만큼의 시간이 소요된다는 차이가 있다. 코딩 테스트에서는 **노드와 간선의 개수가 모두 많으면 우선 순위 큐를 사용하는 다익스트라 알고리즘을 이용하면 유리하고, 노드의 개수가 적으면 플로이드 워셜 알고리즘을 이용하는 것이 낫다.**

---

지금부터는 기타 그래프 알고리즘을 익혀볼텐데, 그 전에 몇몇 자료구조를 알아보자.

### **서로소 집합**

: 수학에서 서로소 집합(Disjoint Sets)이란 공통 원소가 없는 두 집합을 의미한다. **서로소 집합 자료구조는 몇몇 그래프 알고리즘에서 매우 중요하게 사용**된다. 서로소 집합 자료구조는 **union**과 **find**의 연산으로 조작할 수 있는데, union(합집합) 연산은 2개원 원소가 포함된 집합을 하나의 집합으로 합치는 연산이고, find 연산은 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산이다. 그래서, 서로소 집합 자료구조는 **union-find(합치기 찾기) 자료구조** 라고 불리기도 한다. 두 집합이 서로소 관계인지를 확인할 수 있다는 말인 즉슨 각 집합이 어떤 원소를 공통으로 가지고 있는지를 확인할 수 있다는 말이기 때문이다.

서로소 집합 정보가 주어졌을 때, 트리 자료구조를 이용해서 집합을 표현하는 서로소 집합 계산 알고리즘은 아래와 같다.

> 1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다.                                        
> 	1-1. A와 B의 루트 노드 A',B' 를 각각 찾는다.                                                                      
> 	1-2. A'를 B'의 부모 노드로 설정한다. (B'이 A'를 가리키도록 하는 것)                                 
> 2. 모든 union(합집합) 연산을 처리할 때까지 1번과정을 반복한다.

보통, 구현할 때는 **A'와 B' 중 더 번호가 작은 원소가 부모 노드가 되도록 구현하는 경우가 많다**. 예를 들어 설명하는 것이 더 이해가 빠를 것이다. 전체 집합 {1,2,3,4,5,6} 이 6개의 원소로 구성되어 있는 상황을 가정해보자.

> (union 1,4)    (union 2,3)    (union 2,4)    (union 5,6)

이 때, 위와 같이 4개의 union 연산이 있다고 해보자. 각 연산의 의미는 두 원소가 같은 집합이라는 뜻이다. 다시 말해, **그래프**에서 각 **원소는 노드로 표현**되고, '같은 집합에 속한다'는 정보를 담은 **union 연산들은 간선들로 표현**된다. 번호가 큰 노드가 번호가 작은 노드를 간선으로 가리키도록 트리 구조를 이용해 그림을 그려보면 아래와 같다.

![https://blog.kakaocdn.net/dn/bxqYwn/btrdetoeVcN/1bdRJyRDAKszHi4iHR7gAk/img.png](https://blog.kakaocdn.net/dn/bxqYwn/btrdetoeVcN/1bdRJyRDAKszHi4iHR7gAk/img.png)

위 그림을 통해, 전체 원소가 {1,2,3,4} 와 {5,6} 이라는 두 집합으로 나누어지는 것을 알 수 있다. 이렇게 union 연산을 토대로 그래프를 그리면 **'연결성'을 손쉽게 집합의 형태를 확인할 수 있다.** 구체적인 알고리즘의 동작 원리를 단계별로 살펴보면 아래와 같다.

![https://blog.kakaocdn.net/dn/5h7Iv/btrc13rQ16P/XOn6R7ex2mvus15L32NmP0/img.png](https://blog.kakaocdn.net/dn/5h7Iv/btrc13rQ16P/XOn6R7ex2mvus15L32NmP0/img.png)

![https://blog.kakaocdn.net/dn/cb29v5/btrdcOTZytj/NjIZxt9gclKWpsl3s9yI91/img.png](https://blog.kakaocdn.net/dn/cb29v5/btrdcOTZytj/NjIZxt9gclKWpsl3s9yI91/img.png)

이 알고리즘에서 유의할 점은 union 연산을 효과적으로 수행하기 위해, **'부모 테이블'을 항상 가지고 있어야 한다**는 점이다. 또한, 루트 노드를 즉시 계산할 수 없고, **부모 테이블을 계속해서 확인하며 거슬러 올라가야 한다**. 위의 예에서도, 그림에서는 노드3의 부모 노드는 2라고 되어 있지만, 노드2의 부모가 1이기 때문에 최종적으로 노드3의 루트 노드는 1이다. 즉, **서로소 집합 알고리즘**으로 **루트를 찾기 위해서**는 **재귀적으로 부모를 거슬러 올라가야 한다**는 점을 기억하자. 기본적인 서로소 집합 알고리즘의 소스코드는 아래와 같다.

```python
import sys
input = sys.stdin.readline
 
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x
# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
 
 
# 노드의 개수와 간선(union 연산)의 개수 입력받기
node, edge = map(int,input().split())
parent = [0] * (node+1)  # 부모 테이블 초기화 
 
# 부모 테이상에서, 부모를 자기 자신으로 초기화 
for i in range(1,node+1):
    parent[i] = i
 
# union 연산을 각각 수행
for i in range(edge):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
 
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ',end="")
for i in range(1,node+1):
    print(find_parent(parent,i),end=" ")
print()
 
# 부모 테이블 내용 출력
print('부모 테이블:  ',end="")
for i in range(1,node+1):
    print(parent[i],end=" ")
    
'''
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블:  1 1 2 1 5 5
'''
```

이렇게 구현하며느 답은 구할 수 있지만, find 함수가 비효율적으로 동작한다. 최악의 경우에는 find 함수가 모든 노드를 다 확인할 수 있기 때문에 시간 복잡도가 O(V)가 된다. 결과적으로, 현재의 알고리즘을 그대로 이용하게 되면, 노드의 개수가 V개이고, find 혹은 union 연산의 개수가 M개 일때, 전체 **시간복잡도는 O(VM)이 되어 비효율적**이다. 하지만, **경로 합축(Path Compression)기법**을 적용하면 **시간 복잡도를 개선**시킬 수 있다. 경로 압축은 **find 함수를 재귀적으로 호출한 뒤에, 부모 테이블 값을 갱신하는 기법**이다. 경로 압축 함수는 아레와 같다.

```python
def find_parent(parent,x):
	if parent[x] != x :
    		parent[x] = find_parent(parent,parent[x])
    return parent[x]
```

이렇게 함수를 수정하면, 각 노드에 대하여 find 함수를 호출한 이후에, 해당 노드의 루트 노드가 바로 부모 노드가 된다. 전체적으로 개선된 서로소 집합 알고리즘 소스코드는 아래와 같다.

```python
import sys
input = sys.stdin.readline
 
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
 
 
# 노드의 개수와 간선(union 연산)의 개수 입력받기
node, edge = map(int,input().split())
parent = [0] * (node+1)  # 부모 테이블 초기화 
 
# 부모 테이상에서, 부모를 자기 자신으로 초기화 
for i in range(1,node+1):
    parent[i] = i
 
# union 연산을 각각 수행
for i in range(edge):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
 
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ',end="")
for i in range(1,node+1):
    print(find_parent(parent,i),end=" ")
print()
 
# 부모 테이블 내용 출력
print('부모 테이블:  ',end="")
for i in range(1,node+1):
    print(parent[i],end=" ")
 
'''
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블:  1 1 1 1 5 5
'''
```

서로소 집합 알고리즘을 구현할 때, **경로 압축 방법만을 이용해도, 시간 복잡도는 줄일 수 있다**. 이 외에도, 시간 복잡도를 줄일 수 있는 방법이 여러가지 더 있지만, **코딩테스트 수준에서는 경로 압축만 적용해도 충분**하다. 따라서, 비교적 개념과 구현이 간단한 경로 압축 구현은 꼭 기억해 두자.

이러한 **서로소 집합**은 다양한 알고리즘에서 사용될 수 있는데, 대표적으로 서로소 **무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다**는 특징이 있다. (방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별가능하다.) **union 연산**은 그래프에서 간선으로 표현될 수 있으므로, 간선을 하나씩 확인하면서 **두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는 것만으로도 사이클을 판별할 수 있다.** 과정은 아래와 같다.

> 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.                                                           
> 	1-1. 루트 노드가 서로 다르다면, 두 노드에 대하여 union 연산을 수행한다.                           
> 	1-2. 루트 노드가 서로 같다면 사이클(cycle)이 발생한 것이다.                                                       
> 2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

구체적인 원리는 아래와 같다.

![https://blog.kakaocdn.net/dn/cAg1J3/btrdd5H49eX/kvgGE6s9qp2wcy8omSLz50/img.png](https://blog.kakaocdn.net/dn/cAg1J3/btrdd5H49eX/kvgGE6s9qp2wcy8omSLz50/img.png)

![https://blog.kakaocdn.net/dn/ebPpha/btrc9MPK2a2/kQzbXeUSeu5PDXGjYjnUw0/img.png](https://blog.kakaocdn.net/dn/ebPpha/btrc9MPK2a2/kQzbXeUSeu5PDXGjYjnUw0/img.png)

이러한 사이클 판별 알고리즘은 간선의 개수가 E개일 때, **모든 간선을 하나씩 다 확인**하며, **매 간선에 대하여 union 및 find 함수를 호출**하는 방식으로 동작한다. 다시한번 말하지만, 이 알고리즘은 **간선에 방향성이 없는 무방향 그래프에서만 적용 가능하다.** 서로소 집합을 활용한 사이클 판별 코드는 아래와 같다.

```python
import sys
input = sys.stdin.readline
 
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
 
# 노드의 개수와 간선(union 연산)의 개수 입력받기
node, edge = map(int,input().split())
parent = [0] * (node+1)  # 부모 테이블 초기화 
 
# 부모 테이상에서, 부모를 자기 자신으로 초기화 
for i in range(1,node+1):
    parent[i] = i
 
cycle = False # 사이클 발생 여부 
 
for i in range(edge):
    a,b = map(int,input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
        # 사이클이 발생하지 않았다면 합집합(union)수행
    else:
        union_parent(parent,a,b)
 
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
```

>>> 그래프 ②에서 이어서 설명 ...

### **신장 트리**

: 신장 트리(Spanning Tree)란 **하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프**를 의미한다. **모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립 조건**이기도 하기 때문에, 이러한 그래프를 신장 트리라고 부르는 것이다. 예를 들어보자.

![https://blog.kakaocdn.net/dn/bze3RO/btrc6Q0dKav/ujWs7UT7IF2HKkgXA6fXj1/img.png](https://blog.kakaocdn.net/dn/bze3RO/btrc6Q0dKav/ujWs7UT7IF2HKkgXA6fXj1/img.png)

---

### **크루스칼 알고리즘**

다양한 문제 상황에서 가능한 한 최소한의 비용으로 신장 트리를 찾아야 하는데, 이처럼 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘을 '**신장 트리 알고리즘**'이라고 한다. 대표적인 신장 트리 알고리즘으로는 **'크루스칼 알고리즘(Kruskal Algorithm)'**이 있다. 크루스칼 알고리즘은 그리디 알고리즘으로 분류된다. 모든 간선에 대하여 정렬을 수행한 뒤에 **가장 거리가 짧은 간선부터 집합에 포함**시키면 된다. 단, **사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다**. 과정은 아래와 같다.

> 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.                                                               
> 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.                                                  
> 	2-1. 사이클이 발생하지 않는 경우, 최소 신장 트리에 포함시킨다.                                   
> 	2-2. 사이클이 발생하는 경우, 최소 신장 트리에 포함시키지 않는다.                                                
> 3. 모든 간선에 대하여 2번 과정을 반복한다.

크루스칼 알고리즘의 핵심 원리는 가장 거리가 짧은 간선부터 차례대로 집합에 추가하면 된다는 것인데, 사이클을 발생시키는 간선은 제외하고 연결하면 된다. 이렇게 하면, 항상 최적의 해를 보장한다. 구체적인 원리는 아래와 같다.

![https://blog.kakaocdn.net/dn/Fz24h/btrdaFQUSJH/d6ozMzi1sEJLKP92Sf1570/img.png](https://blog.kakaocdn.net/dn/Fz24h/btrdaFQUSJH/d6ozMzi1sEJLKP92Sf1570/img.png)

![https://blog.kakaocdn.net/dn/buytzI/btrc6RriLnQ/xki97ROK0eWN8XUVEzegM0/img.png](https://blog.kakaocdn.net/dn/buytzI/btrc6RriLnQ/xki97ROK0eWN8XUVEzegM0/img.png)

![https://blog.kakaocdn.net/dn/oFM0L/btrdd7suWiZ/TrFNjFOsNSHuPf7d3bo3Y0/img.png](https://blog.kakaocdn.net/dn/oFM0L/btrdd7suWiZ/TrFNjFOsNSHuPf7d3bo3Y0/img.png)

![https://blog.kakaocdn.net/dn/dPW2ul/btrdfHmniTG/mkFm3o7MdGuVUk8q3xi0tk/img.png](https://blog.kakaocdn.net/dn/dPW2ul/btrdfHmniTG/mkFm3o7MdGuVUk8q3xi0tk/img.png)

![https://blog.kakaocdn.net/dn/bspQk2/btrc9fdRa98/GL1EBpQEsF9MvKiOyM2JkK/img.png](https://blog.kakaocdn.net/dn/bspQk2/btrc9fdRa98/GL1EBpQEsF9MvKiOyM2JkK/img.png)

![https://blog.kakaocdn.net/dn/C2WbP/btrc8gKTlm9/TDcXNr9KpovTIZsxKvXFvk/img.png](https://blog.kakaocdn.net/dn/C2WbP/btrc8gKTlm9/TDcXNr9KpovTIZsxKvXFvk/img.png)

위의 예시에소 최소 신장 트리를 만드는데 필요한 비용은 총 159이다. 최소 신장 트리를 만드는데 필요한 비용을 계산하는 크루스칼 알고리즘 코드는 아래와 같다.

```python
import sys
input = sys.stdin.readline
 
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
 
# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int,input().split())
parent = [0] * (v+1)  # 부모 테이블 초기화 
 
# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0
 
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i
 
# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b, cost = map(int,input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))
 
# 간선을 비용순으로 정렬
edges.sort()
 
# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않은 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
 
print(result)
```

**크루스칼 알고리즘**은 간선의 개수가 E개일 때, **O(ElogE)의 시간복잡도**를 가진다. 간선을 정렬하는 작업이 가장 오래 걸리는 부분인데, **E개의 데이터를 정렬했을 때의 시간복잡도가 O(ElogE)이기 때문**이다. 크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복잡도는 정렬하는 시간 복잡도보다 작으므로 무시한다.

---

### **위상 정렬**

: 위상 정렬(Topology Sort)은 **정렬 알고리즘의 일종**이다. 순서가 정해져 있는 일련의 작업을 차례대로 수행하려고 할 때, 사용가능한 알고리즘이다. 즉, **방향 그래프의 모든 노드**를 '**방향성에 거스리지 않도록 순서대로 나열하는 것**'이다. 현실 세계에서는 위상 정렬을 수행하게 되는 전형적인 예시로 '선수과목을 고려한 학습 순서 설정'등이 있다. 일반적으로, 컴공과 커리큘럼에서 '알고리즘' 과목의 선수과목을 '자료구조'로 해두는데, 그래프상에서 각 과목을 노드로 설정하고, 방향성을 갖는 간선을 그릴 수가 있다. 즉, 그래프에서 선후 관계가 있다면, **위상 정렬을 수행하여 모든 선후 관계를 지키는 전체 순서를 계산할 수 있다**.

위상 정렬 알고리즘을 자세히 살펴보기 전에, 먼저 **진입차수(Indegree)**에 대해 알아야 한다. 진입차수란 특정한 노드로 들어오는 간선의 개수를 의미한다. 위상 정렬 알고리즘 과정은 아래와 같다.

> 1. 진입차수가 0인 노드를 큐에 넣는다.                                                                                      
> 2. 큐가 빌 때까지 다음의 과정을 반복한다.                                                                                          
> 	2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.                              
> 	2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

이 때, **모든 원소를 방문하기 전에 큐가 비어버린다면, 사이클이 존재**한다고 판단할 수 있다. 다시 말해, 큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클이 발생한 것이다. 다만, 기본적으로 **위상 정렬 문제에서는 사이클이 발생하지 않는다고 명시하는 경우가 더 많**으므로, 그러한 경우는 고려하지 않고 설명해보겠다. 구체적인 원리는 아래와 같다.

![https://blog.kakaocdn.net/dn/m0wD7/btrdeswzjK1/dNSrbdh4Ml383jJ7kmdGzk/img.png](https://blog.kakaocdn.net/dn/m0wD7/btrdeswzjK1/dNSrbdh4Ml383jJ7kmdGzk/img.png)

![https://blog.kakaocdn.net/dn/tqlzr/btrdd4CGKmj/Emdrzf5XQY8HkuA3fc8bi1/img.png](https://blog.kakaocdn.net/dn/tqlzr/btrdd4CGKmj/Emdrzf5XQY8HkuA3fc8bi1/img.png)

![https://blog.kakaocdn.net/dn/byZbQr/btrdeWYvhiY/0kArmt3JKykRFPJEzkHNKk/img.png](https://blog.kakaocdn.net/dn/byZbQr/btrdeWYvhiY/0kArmt3JKykRFPJEzkHNKk/img.png)

![https://blog.kakaocdn.net/dn/BbBcu/btrc7OgRSf9/8Yn797mrXAgL4cwQDdtW90/img.png](https://blog.kakaocdn.net/dn/BbBcu/btrc7OgRSf9/8Yn797mrXAgL4cwQDdtW90/img.png)

위 과정을 수행하는 동안 **큐에서 빠져나간 노드를 순서대로 출력**하면, 그것이 바로 **위상 정렬을 수행한 결과**가 된다. 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있을 때가 있기 때문에, **위상 정렬의 답안은 여러 가지가 될 수 있다**는 점이 특징이다. 위 예에서는 **1-2-5-3-6-4-7** 과 **1-5-2-3-6-4-7** 이 답이다. 위상 정렬 코드는 아래와 같다.

```python
from collections import deque
import sys
input = sys.stdin.readline
 
# 노드의 개수와 간선의 개수를 입력받기
v,e = map(int,input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
 
# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입차수 1 증가
    indegree[b] += 1
 
# 위상 정렬 하뭇
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 하는 deque 라이브러리 사용
 
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q : 
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in result :
        print(i,end=" ")
 
topology_sort()
```

**위상 정렬의 시간 복잡도는 O(V+E)** 이다. 위상 정렬을 수행할 때는 **차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거**해야 한다. **노드와 간선 모두를 확인**해야 하므로 O(V+E) 만큼의 시간이 소요되는 것이다.
