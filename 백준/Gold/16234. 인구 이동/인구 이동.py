from collections import deque


def bfs(i, j):
    union = []
    union.append((i, j))
    deq.append((i, j))

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and L <= abs(matrix[x][y] - matrix[nx][ny]) <= R
                and visited[nx][ny] == 0
            ):
                visited[nx][ny] = 1
                deq.append((nx, ny))
                union.append((nx, ny))
    if len(union) <= 1:
        return 0
    result = sum(matrix[i][j] for i, j in union) // len(union)
    for i, j in union:
        matrix[i][j] = result
    return 1


N, L, R = list(map(int, input().split(" ")))
matrix = [list(map(int, input().split(" "))) for _ in range(N)]

deq = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day = 0
while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                flag += bfs(i, j)

    if flag == 0:
        break
    day += 1
print(day)
