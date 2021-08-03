import sys
input = sys.stdin.readline

n, k = map(int,input().split())
array_A = list(map(int,input().split()))
array_B = list(map(int,input().split()))

if k==0 : 
    print(sum(array_A))
else:
    answer = sum(array_A)
    sorted_array_A = sorted(array_A) # 12345 --> 오름차순
    rv_sorted_array_B = sorted(array_B,reverse=True) # 66555 --> 내림차순
    for i in range(1,k+1):  # k 번 반복
        a_k_sum = sum(sorted_array_A[:i])  # 오름차순된 배열 A의 i 번째까지의 원소 합
        b_k_sum = sum(rv_sorted_array_B[:i])  # 내림차순정렬된 배열 B의 i 번째까지의 원소 합
        if(a_k_sum < b_k_sum): # b_k_sum 이 더 크다면, 교체한 값이 더 큰 것
            answer = max(answer,b_k_sum+sum(sorted_array_A[i:])) # 기존의 answer와 비교해서 더 큰값으로 업데이트
    print(answer)
