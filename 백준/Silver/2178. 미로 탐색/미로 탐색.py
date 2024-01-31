from collections import deque

N, M = list(map(int, input().split(' ')))
graph = [list(map(int, input())) for _ in range(N)]
dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)
deq = deque([[0, 0]])
while deq:
	x, y = deq.popleft()

	if x == N and y == M:
		break
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
			graph[nx][ny] = graph[x][y] + 1 # 이동 거리 기록
			deq.append([nx, ny])

print(graph[N-1][M-1])