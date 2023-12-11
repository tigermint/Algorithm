import sys
from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    result = [0 for _ in range(m)] # 각 col에 대해 시추관을 뚫었을 때 얻을 수 있는 석유량
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i, j, visited, n, m, land, result)
    answer = max(result)
    return answer

def bfs(x, y, visited, n, m, land, result):

    queue = deque([(x, y)])
    visited[x][y] = 1
    oil = 0
    startY, endY = sys.maxsize, -sys.maxsize
    
    while queue:
        cx, cy = queue.popleft()
        oil += 1
        startY, endY = min(startY, cy), max(endY, cy) # 석유 시작 지점, 마감 지점
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    for col in range(startY, endY + 1): # 해당 col 범위에 대해 석유량 누적
        result[col] += oil
       
