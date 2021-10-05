import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

dp = [x for x in num_list]

for i in range(n):  # 0 부터 n-1 까지 순회하면서 
    for j in range(i):  # j는 0부터 i-1
        if num_list[i] > num_list[j]:  # num_list[i] 값이 num_list[j] 보다 크면,
            dp[i] = max(dp[i], dp[j] + num_list[i])  # dp[i]값 갱신 (dp[i]와 dp[j]와 num_list[i]의 합 중에 큰 값으로 할당)
# print(dp)  # [1, 101, 3, 53, 113, 6, 11, 17, 24, 32]
print(max(dp))
