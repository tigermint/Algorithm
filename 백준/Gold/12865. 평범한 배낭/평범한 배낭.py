N, K = map(int, input().split())
W = [0]; V = [0]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# 완탐으로 풀 수 있지만 경우가 너무 많다
# 경우의 수에 중복이 많음 => dp

for i in range(1, N + 1): # i번째 물건을 사용할 때
    for j in range(1, K + 1): # j 번째 물건을 사용할 때
        if j < W[i]: # 넣을 수 없을 경우 pass
            dp[i][j] = dp[i-1][j] # 이전 최대 가치
        else:
            dp[i][j] = max(dp[i-1][j-W[i]] + V[i], dp[i-1][j]) # 넣지 않았을 때 가치 vs 넣었을 경우 가치
print(dp[N][K])