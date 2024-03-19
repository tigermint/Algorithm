from collections import deque
import copy


def fire_bfs():
    while fire_deq:
        x, y = fire_deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < R
                and 0 <= ny < C
                and not (
                    str(fire_matrix[nx][ny]).isdigit() or fire_matrix[nx][ny] == "#"
                )
            ):
                fire_deq.append((nx, ny))
                fire_matrix[nx][ny] = fire_matrix[x][y] + 1


def person_bfs():

    for x, y in person_deq:
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            return person_matrix[x][y] + 1

    while person_deq:
        x, y = person_deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < R
                and 0 <= ny < C
                and not (
                    str(person_matrix[nx][ny]).isdigit() or person_matrix[nx][ny] == "#"
                )
            ):
                if (
                    str(fire_matrix[nx][ny]).isdigit()
                    and person_matrix[x][y] + 1 >= fire_matrix[nx][ny]
                ):
                    continue
                person_deq.append((nx, ny))
                person_matrix[nx][ny] = person_matrix[x][y] + 1

                if nx == 0 or nx == R - 1 or ny == 0 or ny == C - 1:
                    return person_matrix[nx][ny] + 1
    return False


R, C = list(map(int, input().split()))
matrix = [list(input()) for _ in range(R)]
fire_matrix = copy.deepcopy(matrix)
person_matrix = copy.deepcopy(matrix)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
fire_deq = deque()
person_deq = deque()

for i in range(R):
    for j in range(C):
        if fire_matrix[i][j] == "F":
            fire_deq.append((i, j))
            fire_matrix[i][j] = 0
        elif person_matrix[i][j] == "J":
            person_deq.append((i, j))
            person_matrix[i][j] = 0
fire_bfs()
result = person_bfs()
print(result) if result else print("IMPOSSIBLE")
