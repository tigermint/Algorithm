from collections import deque

N, M = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
matrix = [list(input()) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x1, y1):
    deq = deque([(x1, y1)])
    wave_deq = deque([])
    visited[x1][y1] = 0

    # 칸이 0 이라면 1을 만날 때까지 상하좌우로 퍼져나간다

    while deq:
        x, y = deq.popleft()
        wave_deq.append((x, y))
        while wave_deq:
            wave_x, wave_y = wave_deq.popleft()

            for i in range(4):
                nx = wave_x + dx[i]
                ny = wave_y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                    if matrix[nx][ny] == "0":  # 파동 진행
                        wave_deq.append((nx, ny))
                        visited[nx][ny] = visited[wave_x][wave_y]
                    else:  # 더 이상 파동 진행하지 않음
                        deq.append((nx, ny))
                        matrix[nx][ny] = "0"
                        visited[nx][ny] = visited[x][y] + 1


bfs(x1 - 1, y1 - 1)
print(visited[x2 - 1][y2 - 1])
