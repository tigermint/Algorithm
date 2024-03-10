from collections import deque


def bfs(x, y):
    deq = deque([(x, y)])
    visited[x][y] = 1

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                    deq.append((nx, ny))
                    visited[nx][ny] = 1
                elif matrix[nx][ny] == 1:
                    matrix[nx][ny] = "c"


N, M = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count_list = []
time = 0

while True:
    # 남은 치즈 개수
    count = 0
    for i in range(N):
        count += matrix[i].count(1)
    count_list.append(count)

    if count == 0:
        break

    visited = [[0 for _ in range(M)] for _ in range(N)]

    bfs(0, 0)

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "c":
                matrix[i][j] = 0
    time += 1

print(time)
print(count_list[-2])
