# 처음에는 이런식으로 했다,,각 집과 연관성이 있고, 해당 집의 색깔에 따라 다음 집의 색깔이 결정되는 문제라서 DP 라는 것을 알았고
# 아래와 같이 풀다가, 열추출에서 막혔다... 이를 어떻게 해결할까 해서 구글링을 살짝 했는데, 각 색상마다 따로따로 계산하였다..

n = int(input())
INF = int(1e9)
dp = [INF]*(n+1)
graph = [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n+1):
    # 어떤 식으로 열추출을 할까,, 같은 열(같은색상)이면 안되니까,,
    dp[i] = min(dp[i],min(graph[i-1]))
    
# 구글링을 참고한 풀이
import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
# dp = [INF]*(n+1)
rgb = [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    # 빨간 집
    rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0]
    # 초록 집
    rgb[i][1] = min(rgb[i-1][0],rgb[i-1][2]) + rgb[i][1]
    # 파란 집
    rgb[i][2] = min(rgb[i-1][0],rgb[i-1][1]) + rgb[i][2]
print(min(rgb[n-1]))

# 내 풀이와 다른 점은, 나
# 1) 나는 dp와 rgb 그래프를 따로 따로 받았는데, 그럴 필요가 없이 rgb 자체를 갱신하면서 dp형식으로 풀면됐다.
# 2) 이웃집은 같은 색상으로 칠하지 못하는 것을 해결하려면, 나는 if문을 써서 열추출을 해야한다고 생각했는데, 그것보단, 각 색상에 따라, 예를 들어 빨간색 집을 색칠하고 싶다면
#    이전 집의 초록색과 파란색 값중에 작은 값을 결정하고, 해당 집의 빨간 값과 더해주면 그 값이 그 집을 칠하는 비용으로 갱신되는 로직이다. 색상마다 따로 해주는 것이 키포인트였다.
