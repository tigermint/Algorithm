from itertools import combinations
from collections import deque
import copy


def bfs(x, y):
    virus_spread_matrix[x][y] = 1
    deq = deque([(x, y)])

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < M
                and virus_spread_matrix[nx][ny] == 0
                and visus_spread_visited[nx][ny] == 0
            ):
                deq.append((nx, ny))
                visus_spread_visited[nx][ny] = 1
                virus_spread_matrix[nx][ny] = 2


N, M = list(map(int, input().split()))  # 8 * 8
matrix = [list(map(int, input().split())) for _ in range(N)]
candidates = []
virus = []
wall_cases = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            candidates.append((i, j))
        if matrix[i][j] == 2:
            virus.append((i, j))

# 어디에 세개의 벽을 둘 지 탐색 64 C 3 -> 249,984
# 바이러스가 퍼지는 경우 바이러스의 개수 -> N^2 = 64
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(M)] for _ in range(N)]
safe_area = 0
index = 0
for combi in list(combinations(candidates, 3)):
    virus_spread_matrix = copy.deepcopy(matrix)
    visus_spread_visited = copy.deepcopy(visited)

    for c in combi:
        virus_spread_matrix[c[0]][c[1]] = 1

    # dfs를 통한 virus update
    for v in virus:
        if visited[v[0]][v[1]] == 0:  # 이미 방문 노드 pass
            bfs(v[0], v[1])

    # safe area 연산
    count = 0
    for i in range(N):
        for j in range(M):
            if virus_spread_matrix[i][j] == 0:
                count += 1
    safe_area = max(safe_area, count)
print(safe_area)