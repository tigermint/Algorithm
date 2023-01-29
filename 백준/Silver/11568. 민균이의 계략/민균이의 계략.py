N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    max_num = 0
    for j in range(i):
        if nums[j] < nums[i]:
            max_num = max(max_num, dp[j])
    dp[i] = max_num + 1
print(max(dp))
