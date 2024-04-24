import sys

input = sys.stdin.readline

R, C = list(map(int, input().split()))
matrix = [list(input()) for _ in range(R)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = set(matrix[0][0])
answer = 0


def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] not in visited:
            visited.add(matrix[nx][ny])
            dfs(nx, ny, count + 1)
            visited.remove(matrix[nx][ny])


dfs(0, 0, 1)
print(answer)
