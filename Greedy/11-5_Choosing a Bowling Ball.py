import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ball_list = list(map(int, input().split()))
count = 0

a_index = 0  # ball_list에서 A가 고르는 index 번호 : 초기값 0 부여
for A_ball in ball_list:
    # B는 A가 고르는 index 다음 원소부터 고를 수 있다(중복 방지)
    for B_ball in ball_list[a_index+1:]:
        if(A_ball != B_ball):
            count += 1
    a_index += 1  # B도 다 골랐으면, A 인덱스 1 증가
print(count)  # 총 경우의 수
