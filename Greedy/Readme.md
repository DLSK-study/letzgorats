### **그리디(Greedy) 알고리즘**

: 욕심쟁이 알고리즘이라고도 하는 탐욕 알고리즘은 단순하지만 강력한 문제 해결법이다. 여기서 탐욕적이라는 말은 '**현재 상황에서 지금 당장 좋은 것만 고르는 방법**'을 의미한다. 그리디 알고리즘은 매 순간 가장 좋아보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.

그리디 알고리즘은 기준에 따라 가장 좋은 것을 선택하는 알고리즘으로, 문제에서 '가장 큰 순서대로' 혹은 '가장 작은 순서대로' 와 같은 기준을 문제에서 알게 모르게 제공해준다. 정렬 알고리즘을 사용했을 때, 효과적으로 풀 수 있어, 보통 **정렬 알고리즘과 짝을 이루어 출제**되곤 한다.

**대표적인 그리디 알고리즘 예제 - 1) 동전 거스름돈 문제**

```python
import sys
input = sys.stdin.readline
 
coin = [500, 100, 50, 10]
N = int(input())
standard = 0
answer = 0
while(N != 0):
    answer += N // coin[standard]
    N %= coin[standard]
    standard += 1
 
print(answer)
```

물론 위 코드에서 대체로 최적의 동전개수를 구할 수 있지만, 800원을 거슬러 주려고 할 때, 동전이 500원, 400원, 100원이 있다면, 800 = 500 + 100 + 100 + 100 으로 4개라고 출력하지만, 실제로는 400원짜리 2개를 거슬러주는 것이 더 최적의 해다.

**그리디 알고리즘은 이처럼 나중을 고려하지 않고 그 순간순간에 가장 베스트인 것을 고르는 알고리즘이기 때문에 정당성 부분에서 모든 알고리즘 문제에 적용할 수 있는 것은 아니다**. 이 부분은 나중에 **동적 계획법(메모제이션)을 다룰 때 더 최적의 개수를 구하는 방법을 배워보도록** 하자.

위 코드의 시간복잡도는 coin의 개수 에 따라 달라지므로 O(n)이라고 할 수 있겠다.

※ 그리디 알고리즘 문제를 효율적으로 풀려면, (나의 판단)

▶ 경우의 수를 구하는 방법과 유형을 파악하자.

(ex) 리스트 안의 요소로 만들 수 있는 새로운 수

(ex) 힙,덱,스택,큐 등의 라이브러리 사용하는데에 자연스러워지기

▶ 정렬을 효과적으로 이용하자

(ex) sort보단 sorted를 애용하자

(ex) 정렬 중에서도 복잡도가 낮은 정렬을 이용해보자.

**<그리디 알고리즘의 종류>**

1. Fractional Knapsack Problem (=> 거스름돈 문제)

2. 시간표 배정

3. 수학적 성질이 최적해를 보장하는 경우

4. Huffman Code

5. 다익스트라

6. MST(Kruskal, Prim)

7. 최대 유량

**<그리디 백준 문제 추천>**

[11047번 동전 0](https://www.acmicpc.net/problem/11047)

[2875번 대회 Or 인턴](https://www.acmicpc.net/problem/2875)

[10610번 30](https://www.acmicpc.net/problem/10610)

[1783번 병든 나이트](https://www.acmicpc.net/problem/1783)

[11000번 강의실 배정](https://www.acmicpc.net/problem/11000)

[1931번 회의실 배정](https://www.acmicpc.net/problem/1931)

[11399번 ATM](https://www.acmicpc.net/problem/11399)

[2217번 로프](https://www.acmicpc.net/problem/2217)

[13458번 시험감독](https://www.acmicpc.net/problem/13458)

[1946번 신입 사원](https://www.acmicpc.net/problem/1946)

[4796번 캠핑](https://www.acmicpc.net/problem/4796)

[1541번 잃어버린 괄호](https://www.acmicpc.net/problem/1541)

[12845번 모두의 마블](https://www.acmicpc.net/problem/12845)

[2873번 롤러코스터](https://www.acmicpc.net/problem/2873)

[1744번 수 묶기](https://www.acmicpc.net/problem/1744)

[1700번 멀티탭 스케줄링](https://www.acmicpc.net/problem/1700)

[1969번 DNA](https://www.acmicpc.net/problem/1969)
