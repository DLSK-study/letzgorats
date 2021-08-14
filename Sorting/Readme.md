**정렬(Sorting)이란 ?**

**: 데이터를 측정한 기준에 따라서 순서대로 나열하는 것**으로, 프로그램을 작성할 때 가장 많이 사용되는 알고리즘 중 하나다. 정렬 알고리즘은 굉장히 다양한데, 이 중에서 많이 사용하는 정렬은 **선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬** 등이 있다. 정렬 알고리즘을 잘 공부하면, 알고리즘의 효율을 높일 수 있다. 또한, 코딩 테스트에서의 정렬 알고리즘 문제는 어느 정도 정해진 답이 있어서, 외워서 잘 풀어낼 수 있는 문제라고도 할 수 있다.

오름차순을 기준으로 각 정렬을 살펴보자.

# **선택 정렬(Selection Sort)**

: 데이터가 무작위로 있을 때, 그 중 가장 작은 값을 선택해 맨 앞에 있는 값과 바꾸고, 그 다음 작은 값을 선택해 앞에서 두 번째 값과 바꾸는 과정을 계속 반복하는 것이다. 즉, **매번 가장 작은 값을 선택한다는 의미**에서 "선택 정렬(Selection sort)"이라고 한다. 이 때, 데이터가 N개 있다고 하면, 반복하는 과정은 N-1 번을 하게 된다.

파이썬으로 구현한 코드는 아래와 같다.

```python
array = [7,5,9,0,3,1,6,4,2,8]
 
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):  # 안쪽 for문은 가장 작은 원소의 index 값 찾는 과정
        if array[min_index] > array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index] , array[i]  # swap
 
print(array)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

※ 여기서 파이썬에서 swap은 다른 프로그래밍 언어와는 달리, 명시적으로 임시 저장용 변수를 만들지 않아도 된다.

예를 들어, 자바에서는 아래와 같이 swap을 처리해야 한다. temp라는 변수로 임시로 값을 저장해야만 올바르게 값이 바뀌는데, 파이썬에서는 그런 과정 없이 그냥 한번에 바꿀 수 있다.

```java
public class Swap { 
	public static void swap(int[] arr) { 
		int temp = arr[0]; 
    arr[0] = arr[1]; 
    arr[1] = temp; 
    } 
}
```

- 선택정렬은 모든 데이터가 정렬이 되어있어도 무조건 전체 리스트를 순회해가며 검사하기 때문에 최선의 경우든 최악의 경우든 **한결같이 O(n²)의 시간복잡도**를 가지고 있다.
- 코딩테스트에서는 가장 작은 데이터를 찾는 일이 잦으므로 선택정렬 소스코드 형태에 익숙해질 필요가 있다.
- **~~선택 정렬은 교환의 횟수가 버블 정렬이나 삽입 정렬 보다 작다.~~**
- 자료 이동 횟수가 고정적이다. **( + )**
- 안정성을 만족하지 않는다, 즉 값이 같은 레코드가 있는 경우에 상대적인 위치가 변경될 수 있다. ( 같은 3이라도 서로 다른 각각의 3으로 해석하는 문제 등에서 ) **( - )**

![https://blog.kakaocdn.net/dn/pR2Be/btra35qZI3d/ePy8Ley1ZKaqssyjwkNzKK/img.gif](https://blog.kakaocdn.net/dn/pR2Be/btra35qZI3d/ePy8Ley1ZKaqssyjwkNzKK/img.gif)

선택 정렬

---

# **삽입 정렬(Insertion Sort)**

****: 삽입 정렬은 **필요할 때만 위치를 바꾸므로**, 정렬이 어느 정도 되어있냐에 따라 더 효율적인 실행시간을 가질 수 있다. 삽입 정렬은 **특정한 데이터를 적절한 위치에 '삽입'한다는 의미**에서 '삽입 정렬(Insertion sort)' 라고 한다. 삽입 정렬의 특징은 두번째 데이터부터 시작하는데, 첫 번째 데이터가 그 자체로 정렬되어 있다고 판단하기 때문이다. 

삽입 정렬의 과정은 대략 아래와 같다.

1. 0번 인덱스는 건너뛴다.
2. 0~1번 인덱스 중 1번 인덱스 값이 들어가야할 위치를 찾아서 넣는다.
3. 0~2번 인덱스 중 2번 인덱스 값이 들어가야할 위치를 찾아서 넣는다.…
4. 0~n번 인덱스 중 n번 인덱스 값이 들어가야할 위치를 찾아서 넣는다.

이와 같이 적절한 위치에 찾아서 넣는 과정을 N-1 번 반복하게 되면, 모든 데이터가 정렬되게 된다. 파이썬으로 구현한 코드는 아래와 같다.

```python
array = [7,5,9,0,3,1,6,4,2,8]
 
for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하며 반복
        if(array[j] < array[j-1]):  # 한칸씩 왼쪽으로 이동하는데, 자기보다 큰 값이 있으면 자리 바꾸면서 계속 진행
            array[j], array[j-1] = array[j-1] , array[j]
        else: # 오름차순으로 정렬하는 상황이므로, 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)
```

- 삽입정렬은 **최선의 경우** 전체 자료를 한번만 순회하면 되기때문에 **O(n)의 시간복잡도**를 가지지만 **최악의 경우 O(n²)의 시간복잡도**를 가진다. ( 거의 정렬이 되어 있으면, 이동 없이 1번의 루프만 비교함으로써, O(n-1)이므로 )
- 자료 개수가 적거나 거의 정렬이 되어 있는 상태라면, 퀵 정렬 보다도 더 효율적인 방법이 삽입 정렬이다. ( **+** )
- 안정적인 정렬 방법이다. ( **+** )
- 최선의 경우 O(N)이라는 엄청나게 빠른 효율성을 가지고 있다. ( **+** )
- 비교적 많은 레코드들의 이동을 포함한다. ( -**** )
- 레코드 수가 많고 크기가 클 때, 적합하지 않은 정렬 방법이다. ( -**** )

![https://blog.kakaocdn.net/dn/RiOKw/btra1ZR1wCQ/2kbezTOJP2XtO0JkdXShAK/img.gif](https://blog.kakaocdn.net/dn/RiOKw/btra1ZR1wCQ/2kbezTOJP2XtO0JkdXShAK/img.gif)

삽입 정렬

---

# **퀵 정렬(Quick Sort)**

****: 퀵 정렬은 병합 알고리즘(Merge Sort) 와 함께 대부분의 프로그래밍 언어에서 **정렬 라이브러리의 근간**이 되는 알고리즘이다. 퀵 정렬은 기준을 설정한 후, 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다. 이 때, 설정된 **기준값을 피벗(pivot)**이라고 하는데, 합병 정렬(Merge Sort)와는 다르게 비균등하게 분할하는 것이 특징이다. 즉, 정리하자면, **하나의 리스트를 피벗(pivot)을 기준으로 두 개의 비균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법이다.**

**이 때, 정렬하는 과정은 앞선 과정과 똑같이 반복한다. ( 왼쪽 파트에서 새로운 피벗을 정하고, 같은 과정 반복, 오른쪽 파트에서 새로운 피벗을 정하고, 같은 과정 반복)** 

퀵 정렬 과정은 다음 3단계로 구분지을 수 있다.

1. **분할(Divide)**: 입력 배열을 피벗을 기준으로 비균등하게 2개의 부분 배열(피벗을 중심으로 왼쪽: 피벗보다 작은 요소들, 오른쪽: 피벗보다 큰 요소들)로 분할한다.
2. **정복(Conquer)**: 부분 배열을 정렬한다. 부분 배열의 크기가 충분히 작지 않으면 순환 호출 을 이용하여 다시 분할 정복 방법을 적용한다.
3. **결합(Combine)**: 정렬된 부분 배열들을 하나의 배열에 합병한다.순환 호출이 한번 진행될 때마다 최소한 하나의 원소(피벗)는 최종적으로 위치가 정해지므로, 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.

퀵 정렬은 **재귀함수의 로직**과 비슷한데, 재귀함수에서도 종료조건이 가장 중요하다고 했는데, 퀵 정렬에 대입해본다면, 현재 **리스트의 데이터 개수가 1개**인 경우, 분할이 불가능하므로 곧, **종료조건**이 된다.

퀵 정렬을 파이썬으로 구현한 코드는 아래와 같다.

```python
array = [7,5,9,0,3,1,6,4,2,8]
 
def quick_sort(array,start,end):
    if start >=end : # 원소가 1개인 경우 종료
        return 
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1 # 왼쪽은 피벗 다음 원소부터 오른쪽으로 진행방향
    right = end # 오른쪽은 맨 끝 부분부터 왼쪽으로 진행방향
 
    while left <= right : # 왼쪽과 오른쪽값이 교차되기 전까지 반복 
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <=end and array[left] <= array[pivot]:
            left+=1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -=1
        if left > right : # 교차되어서 엇갈렸다면, 작은 데이터와 피벗을 교체
            array[right] , array[pivot] = array[pivot] , array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)
quick_sort(array,0,len(array)-1)
print(array)
 
# 파이썬틱한 퀵 정렬 소스 코드
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [ x for x in tail if x <= pivot ] # 분할된 왼쪽 부분
    right_side = [ x for x in tail if x > pivot ] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
array = [7,5,9,0,3,1,6,4,2,8]
print(quick_sort(array))
```

- 퀵정렬은 **최선의 경우** (분할이 일어날 때마다 정확히 왼쪽과 오른쪽이 절반씩 분할되는 경우)에는 **O( nlog n )의 시간복잡도**를 가지지만 **최악의 경우** ( 분할이 일어날 때마다 계속 왼쪽과 오른쪽이 불균형이 심하게 분할되는 경우) **O(n²)의 시간복잡도**를 가진다. (거의 정렬이 되어 있으면, 매우 느리게 동작한다. 왼쪽과 오른쪽 불균형이 심하므로)
- 속도가 빠르다. 다른 정렬방법과 비교해서도 속도가 준수한 편이다. ( **+** )
- 추가 메모리 공간을 필요로 하지 않는다. (퀵 정렬은 O(log n)만큼의 메모리를 필요로 한다. ) ( **+** ) -> (병합정렬은 원소의 개수만큼 리스트를 쪼개고 따로 저장하고 있어야 하기 때문에 임시배열에 원본배열을 계속해서 옮겨주면서 정렬을 한다.)
- "정렬된 리스트"에 대해서는 퀵 정렬의 불균형 분할에 의해 오히려 수행시간이 더 많이 걸린다. ( ****- )
- 기준값(Pivot)에 따라서 시간복잡도가 크게 달라진다. Pivot이 적당하게 이상적인 값을 선택했다면 O(nlogn) 의 시간복잡도를 갖지만, 최악의 경우에는 O(n²)의 시간복잡도를 가진다. ( - ) —> **** 해결방법) 리스트 내의 몇 개의 데이터 중에서 크기순으로 중간 값(medium)에 해당하는 값을 피벗으로 선택한다.

![https://blog.kakaocdn.net/dn/pVLkC/btrbahw8AWl/ja7t1AKMb8jv8Es3RKk8H0/img.gif](https://blog.kakaocdn.net/dn/pVLkC/btrbahw8AWl/ja7t1AKMb8jv8Es3RKk8H0/img.gif)

퀵 정렬

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/71c7ecc4-cb8a-41d9-86c1-4505efffef1b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/71c7ecc4-cb8a-41d9-86c1-4505efffef1b/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8fa7d48b-8036-4ec4-b172-64c7cd106570/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8fa7d48b-8036-4ec4-b172-64c7cd106570/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/30eb3724-0333-4197-9d46-e7663fac281f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/30eb3724-0333-4197-9d46-e7663fac281f/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75903323-3b5e-4139-a35f-80a65124d87d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75903323-3b5e-4139-a35f-80a65124d87d/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb7d869e-3c60-4218-ac11-2e1d337a11d8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb7d869e-3c60-4218-ac11-2e1d337a11d8/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5eb25fe9-6567-4b6b-9986-1a737473a3bd/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5eb25fe9-6567-4b6b-9986-1a737473a3bd/Untitled.png)

# **계수 정렬(Count Sort)**

---

****: 계수 정렬은 특정한 조건이 부합할 때만 사용가능하지만, **매우 빠른 정렬 알고리즘**이다. 이 때, 특정한 조건이라함은 **"정수 형태로 표현할 수 있을 때" 만 사용할 수 있다**는 것을 뜻한다. 보통 가장 큰 데이터와 가장 작은 데이터의 차이가 100만 을 넘지 않을 때 효과적이다. 계수 정렬은 앞선 정렬 알고리즘 처럼, 데이터 값을 이동하고 비교하면서 정렬하는 방식이 아니다. 계수 정렬은 **별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는 특징** 있다.

예를 들어 설명해보자면, 아래와 같은 데이터가 나열되어 있다고 하자.

```
0 12 2 3 8 9 4 3 11 0 1 2 3 5 7 6 3 10 2 8 7 9 12 8
```

위 데이터 리스트 중에서 **가장 작은 값은 0 , 가장 큰 값은 12** 이므로 우리에게 필요한 별도의 리스트는 0부터 12까지 다 담을 수 있는 **길이가 13인 별도의 리스트가 필요한 셈**이다. 이 때, 별도의 리스트의 모든 값은 0으로 초기화 한다.

파이썬으로 코드를 나타내보면, 아래와 같다.

```python
number = [0,12,2,3,8,9,4,3,11,0,1,2,3,5,7,6,3,10,2,8,7,9,12,8]
max_num = max(number)
count_list = [0] *(max_num+1) # 최댓값보다 1 큰 별도의 리스트 생성
 
for num in number:
    count_list[num] += 1
print(count_list)  # [2, 1, 3, 4, 1, 1, 1, 2, 3, 2, 1, 1, 2]
 
for num in range(len(count_list)):
    for cnt in range(count_list[num]):
        print(num,end=" ")
# 0 0 1 2 2 2 3 3 3 3 4 5 6 7 7 8 8 8 9 9 10 11 12 12
```

- 계수 정렬은 비교를 하지 않고 정렬하므로 O(N+데이터 중 최대값의 크기(K)) = O(N) 이라는 시간복잡도를 갖게 된다. ( 정렬법 중에 엄청나게 빠른 편에 속한다. 하지만, 제한 조건이 까다롭다. ) ( + )
- 데이터의 크기가 많이 중복되어 있거나 동일한 값이 여러개 등장할 때, 사용하면 효과적인 알고리즘이다. ( + )
- 숫자 개수를 저장해야 할 별도의 공간과, 결과를 저장할 별도의 공간 등 추가적인 메모리가 필요하다. ( - )
- 메모리 낭비를 많이 하게 될 수 있다. ( - ) --> ( 예를 들어, [ 1, 2, 3, 4, 999999 ] 인 경우에는 999999 때문에 숫자의 개수를 저장해야 할 배열의 크기가 최소 100만개는 되어야 하고, 이 때, 안 쓰는 낭비되는 인덱스가 너무 많이 발생하게 된다. )

    ---

**총 정리**

![https://blog.kakaocdn.net/dn/cSmFCw/btrbbT33oUw/gukPP8rX6tFnKKEWQVRcD1/img.gif](https://blog.kakaocdn.net/dn/cSmFCw/btrbbT33oUw/gukPP8rX6tFnKKEWQVRcD1/img.gif)

각 상황에 따른 정렬 알고리즘

![https://blog.kakaocdn.net/dn/Eu2Pw/btra8zykjk4/Aky4YKLGmLOYkAyladXlV0/img.png](https://blog.kakaocdn.net/dn/Eu2Pw/btra8zykjk4/Aky4YKLGmLOYkAyladXlV0/img.png)

각 정렬의 장단점

![https://blog.kakaocdn.net/dn/cjS2SC/btra1alkP02/8NbDPxahuGFKYTKiKXojKK/img.png](https://blog.kakaocdn.net/dn/cjS2SC/btra1alkP02/8NbDPxahuGFKYTKiKXojKK/img.png)

각 정렬의 시간 복잡도

---

**파이썬의 정렬 라이브러리**

**:** 파이썬은 기본 정렬 라이브러리로 sorted() 와 sort() 를 제공한다. 둘 다 시간 복잡도 O(nlogn)을 보장해준다는 특징이 있고 sorted() 는 반환 값이 있는 반면에, sort()는 반환 값 없이 내부 원소가 바로 정렬되는 특징이 있다.

```python
array = [7,5,9,0,3,1,2,6,8,4]
result = array.sort()
print(result)  # None 이 출력된다.
```

```python
array = [7,5,9,0,3,1,2,6,8,4]
result = sorted(array) 
print(result)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]이 출력된다.
```

이 외에도, key 매개변수를 입력으로 어느 부분을 기준으로 정렬할지 정해주는 함수도 내장하고 있다.

정렬 라이브러리는 항상 최악의 경우에도 **O(nlogn)의 시간복잡도를 보장**해주며 이미 잘 작성된 함수이다.

코딩 테스트의 경우에는 일반적으로 3가지 문제 유형으로 나타낼 수 있다.

1. 정렬 라이브러리로 풀 수 있는 문제 - 그냥 정렬 라이브러리 사용하면 된다.
2. 정렬 알고리즘의 원리를 물어보는 문제 - 각 정렬의 원리를 알아야 풀 수 있다.
3. 더 빠른 정렬이 필요한 문제 - 퀵 정렬기법으로도 풀지 못하고, 계수 정렬 등을 사용하거나 기존 정렬 알고리즘에서 구조적인 개선을 거쳐야 한다.
