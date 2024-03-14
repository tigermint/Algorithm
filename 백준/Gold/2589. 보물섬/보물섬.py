from collections import deque
import sys


def bfs(i, j):
    global N, M
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    deq = deque([(i, j)])
    visited[i][j] = 0
    result = 0

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < M
                and matrix[nx][ny] == "L"
                and visited[nx][ny] == -1
            ):
                deq.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                result = max(result, visited[nx][ny])

    return result


N, M = list(map(int, sys.stdin.readline().split()))
matrix = [list(sys.stdin.readline()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)
