N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
def dfs(result, idx):
    global count
    if idx >= N:
        return
    result += nums[idx]
    if result == S:
        count += 1
    dfs(result - nums[idx], idx + 1)
    dfs(result, idx + 1)

dfs(0, 0)
print(count)