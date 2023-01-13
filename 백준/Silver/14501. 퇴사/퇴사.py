N = int(input())
consults = [list(map(int, input().split())) for _ in range(N)]
max_profit = 0
def dfs(profit, day):
    global max_profit
    if day >= N:
        max_profit = max(profit, max_profit)
        return
    
    # 선택 x
    dfs(profit, day + 1)
    # 선택 o
    if day + consults[day][0] <= N:
        dfs(profit + consults[day][1], day + consults[day][0])

dfs(0, 0)
print(max_profit)