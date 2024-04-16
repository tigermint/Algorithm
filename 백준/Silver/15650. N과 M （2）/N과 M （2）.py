N, M = list(map(int, input().split()))
nums = [i for i in range(1, N + 1)]

def dfs(seq, idx):
    if len(seq) == M:
        print(*seq)
        return
    if idx == N:
        return

    dfs(seq + [nums[idx]], idx + 1)
    dfs(seq, idx + 1)


dfs([], 0)
