### **순차 탐색**

이진탐색 알고리즘을 배우기 전에 가장 기본 탐색 방법인 순차 탐색 방법에 대해 알아보자. **순차 탐색**이란, **리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례로 확인하는 방법**이다. 말그대로, 순차적으로 탐색을 한다는 의미인데, count() 함수를 이용할 때도 내부에서는 순차 탐색이 수행될 정도로 자주 사용된다. N개의 데이터에서 최대 N번의 비교 연산이 필요하므로 순차 탐색의 시간복잡도는 최악의 경우, O(N)이다. 순차 탐색 코드는 아래와 같다.

```python
import sys
input = sys.stdin.readline
# 순차 탐색 소스코드 구현
def sequential_search(n,target,array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target :
            return i + 1  # 현재의 위치 반환(인덱스는 0부터 시작하므로 1더하기)
 
print("생성할 원소개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])  # 원소의 개수
target = input_data[1]
 
print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()
 
# 순차 탐색 수행 결과 출력
print(sequential_search(n,target,array))
```

### **이진 탐색**

이진 탐색은 순차 탐색과는 다르게 배열 내부의 **데이터가 정렬되어 있어야만 사용할 수 있는** 알고리즘이다. 이진 탐색은 **탐색 범위를 절반씩 좁혀가며** 데이터를 탐색하는 특징이 있다. 위치를 나타내는 **변수 3개를 사용**하는데, 탐색하고자 하는 범위의 **시작점, 중간점** 그리고 **끝점**이다. 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것이 이진 탐색의 과정이다.

![https://blog.kakaocdn.net/dn/9xuz5/btrduU0HGpj/dTMi2tKTRi4VQsEE877lkK/img.png](https://blog.kakaocdn.net/dn/9xuz5/btrduU0HGpj/dTMi2tKTRi4VQsEE877lkK/img.png)

위 과정에서 전체 데이터의 개수는 10개이지만, 이진 탐색을 이용해 총 3번의 탐색만에 원소를 찾을 수 있었다. **이진 탐색**의 **시간복잡도는 O(logN)**으로, 절반씩 데이터를 줄어들도록 만든다는 점은 앞서 다룬 퀵정렬과 공통점이 있다. 이진 탐색을 구현하는 방법에는 2가지가 있는데, 하나는 **1)재귀함수를 이용하는 방법**이고, 다른 하나는 단순히 **2)반복문을 사용하는 방법**이다.

먼저, 1) 재귀함수를 이용하는 코드는 아래와 같다.

```python
import sys
input = sys.stdin.readline
 
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start + end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target : 
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)
 
# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
# 전체 원소 입력받기
array = list(map(int,input().split()))
 
# 이진 탐색 수행 결과 출력
result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

여기서 몫만 구하기 위해 몫 연산자( // )를 사용했는데, 팁을 주자면, int()함수를 이용하는 것보다 훨씬 더 빠르다고 한다. 몫 연산을 할 때는 '//'를 애용하자.

다음은, 2) 단순하게 반복문을 사용한 코드이다.

```python
import sys
input = sys.stdin.readline
 
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array,target,start,end):
    while start <=end:
        mid = (start + end) // 2 
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target :
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
        # 중간점의 값도가 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid+1
    return None
    
# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
# 전체 원소 입력받기
array = list(map(int,input().split()))
 
# 이진 탐색 수행 결과 출력
result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

### **코딩 테스트에서의 이진 탐색**

단순히 앞의 코드를 보고, 비교적 이진 탐색은 쉽다고 느낄 수 있지만, 존 벤틀리(「생각하는 프로그래밍」(인사이트 2014)의 필자)의 말에 따르면, 제대로 이진 탐색 코드를 작성한 프로그래머는 10% 내외라 할 정도로 실제 구현은 까다롭다. 이진 탐색은 코딩테스트에서 단골로 나오는 문제이기도 하고 다른 알고리즘에서도 이진 탐색 알고리즘은 적용되기 때문에, 가급적 외우는 편이 낫다. 탐색 범위가 2000만을 넘어가면 이진 탐색으로 문제에 접근해야 하며, 처리해야 할 데이터의 개수나 값이 1000만 단위 이상으로 넘어가면 이진탐색처럼 O(logN)의 속도를 내야 하는 알고리즘을 떠올려야 문제를 풀 수 있는 경우가 많다.

### **트리 자료구조**

이진 탐색의 전제 조건은 데이터의 정렬이라고 했다. **데이터베이스**는 내부적으로 대용량 데이터 처리에 적합한 **트리 자료구조를 이용하여 항상 데이터가 정렬**되어 있다. 따라서, 데이터베이스에서의 탐색은 이진 탐색과는 조금 다르지만, **이진 탐색과 유사한 방법**을 이용해 탐색을 항상 빠르게 수행하도록 설계되어 있어서 데이터가 많아도 **탐색속도가 빠른 것**이다. **트리 자료구조**는 **그래프 자료구조의 일종**으로 데이터베이스 시템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용된다. 아래 그림은 트리의 구조와 특징이다.

![https://blog.kakaocdn.net/dn/HHnc1/btrdtKc0upZ/SpXvtHX7HMP6Ywdhh0KH10/img.png](https://blog.kakaocdn.net/dn/HHnc1/btrdtKc0upZ/SpXvtHX7HMP6Ywdhh0KH10/img.png)

### **이진 탐색 트리**

트리 자료구조 중에 가장 간단한 형태가 이진 탐색 트리이다. 보통 이진 탐색 트리는 다음과 같은 특징을 가진다.

- 부모 노드보다 왼쪽 자식 노드가 작다.
- 부모 노드보다 오른쪽 자식 노드가 크다.

좀 더 간단하게 표현하면, **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드**가 성립해야지 이진탐색 트리라 할 수 있다.

![https://blog.kakaocdn.net/dn/cWDPEB/btrdqRcnx9P/ooHxpULeBfKYkNN2qWCo7K/img.png](https://blog.kakaocdn.net/dn/cWDPEB/btrdqRcnx9P/ooHxpULeBfKYkNN2qWCo7K/img.png)

위 그림에서도 17 < 30 < 48 로 이진 탐색 트리가 성립하는 것을 볼 수 있다. 이진 탐색 트리에 데이터를 넣고 빼는 방법은 알고리즘보다는 자료구조에 가깝다. 이진 탐색 트리 자료구조를 구현하라고 요구하는 문제는 드물기 때문에, 이진 탐색 트리가 미리 구현되어 있다고 가정하고, **그 구조에서 데이터를 조회하는 과정**을 살펴보겠다.

![https://blog.kakaocdn.net/dn/cs5Qvh/btrdqgwJ4J8/cosd4Li6DV8WnypR08sXxk/img.png](https://blog.kakaocdn.net/dn/cs5Qvh/btrdqgwJ4J8/cosd4Li6DV8WnypR08sXxk/img.png)

![https://blog.kakaocdn.net/dn/GaKcP/btrdqLDH1Ja/7UfcKIZNvYH28XdO9UJXNk/img.png](https://blog.kakaocdn.net/dn/GaKcP/btrdqLDH1Ja/7UfcKIZNvYH28XdO9UJXNk/img.png)

공식에 따라 루트 노드부터 왼쪽 자식 노드 혹은 오른쪽 자식 노드로 이동하며 반복적으로 방문한다. **자식 노드가 없을 때까지 원소를 찾지 못했다면, 이진 탐색 트리에 원소가 없는 것**이다.

이상으로, 이진 탐색에 대해 알아보았다.
