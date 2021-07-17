import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for hour in range(0, N+1):
    for minutes in range(0, 60):
        for seconds in range(0, 60):
            if('3' in str(hour) or '3' in str(minutes) or '3' in str(seconds)):  # 3이 포함되어 있으면
                cnt += 1  # count한다.
print(cnt)
