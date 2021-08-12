# 못풀었다..단순하게 역순으로 리스트를 살펴봤고, 탐색하고 있는 전투력값이 다음 전투력 값보다 크면
# count +1 을 해주는 방법으로 풀었지만, dp를 활용하지 않았고 역시 틀렸다.
# 구글링을 해보니까, LIS 문제로, Longest Increasing Subsequence 의 약자로 한글로는 ‘최장 증가수열’, 또는 ‘최대 증가 부분수열’로 불린다. 
'''
예를 들어 원 배열이 [1,4,6,8,3,5,6,7] 일 때, [1,6,8],[4,6,8],[1,7]은 증가 부분수열인데, 이 중 가장 긴 부분열은 [1,3,5,6,7] 이 된다. 이때 중간의 [4,6,8] 등은 생략한 것을 알 수 있다. 
일반적으로 최장 증가 부분 수열의 길이가 얼마인지 푸는 간편한 방법은 DP를 이용하는 것입니다.
아래에서 length[i] 는 i번째 인덱스에서 끝나는 최장 증가 부분 수열의 길이를 의미합니다.
for (int k = 0; k < n; k++){
	length[k] = 1;
    for (int i = 0; i < k; i++){
        if(arr[i] < arr[k]){
            length[k] = max(length[k], length[i] + 1);
        }        
    }
} dp lis 문제 국룰 패턴
주어진 배열에서 인덱스를 한 칸씩(k+=1) 늘려가면서 확인합니다. 
그리고 내부 반복문으로 k보다 작은 인덱스들을 하나씩 살펴 보면서 
arr[i] < arr[k]인 것이 있을 경우, length[k] 를 업데이트합니다.
----업데이트 기준----
(1) i번째 인덱스에서 끝나는 최장 증가 부분 수열의 마지막에 arr[k]를 추가했을 때의 LIS 길이와
(2) 추가하지 않고 기존의 length[k] 값
둘 중에 더 큰 값으로 length[k] 값을 업데이트합니다.

O(n^2)의 알고리즘은 실행시간이 10초 이상 소요된다고 알려져 있습니다.  ----> DP로 LIS를 풀 수 있는 문제 : (2565번 문제는 n이 100개 이하로 제한됨)
2565번 - 전깃줄 https://www.acmicpc.net/problem/2565

이분 탐색으로 lis 문제 풀면, 일반적으로 시간복잡도가 O(log n) 이라고 알려져 있으므로, 
이 문제의 시간 복잡도를 O(nlog n)으로 개선시킬 수 있게 됩니다.


'''
# dp 풀이 ... 1024ms 
import sys
input = sys.stdin.readline

n = int(input())
soldier = list(map(int,input().split()))
dp=[0]*(n+1)
count = 0
for i in range(n):
    for j in range(i):
        if soldier[i] < soldier[j]:
            dp[i] = max(dp[i],dp[j]+1)
            # print(i,dp[i])
        
print(n-max(dp)-1)


# 이진 탐색으로 푼 풀이 -- 76ms
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right  # bisect 라이브러리 기억해두자.

n = int(input())
soldier = list(map(int,input().split()))
soldier = soldier[::-1]
lis = [soldier[0]] # 초기값은 맨 처음 값 
for i in range(1,n):
    if(lis[-1]<soldier[i]):
        lis.append(soldier[i])
    else:
        index = bisect_left(lis,soldier[i]) # 정렬된 순서를 유지하면서 리스트 lis에 데이터 soldier[i] 삽입할 가장 왼쪽 인덱스 찾기
        lis[index]=soldier[i]

print(n-len(lis))
