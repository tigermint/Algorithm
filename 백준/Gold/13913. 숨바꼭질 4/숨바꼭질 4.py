from collections import deque


def bfs(current):
    deq = deque([current])
    visited[current] = -2  # 시작점

    while deq:
        current = deq.popleft()
        if current == K:  # 발견
            # 경로 찾아주기
            while current != -2:
                path.append(current)
                current = visited[current]
            return

        for next_current in [current - 1, current + 1, current * 2]:
            if 0 <= next_current <= 100000 and visited[next_current] == -1:
                deq.append(next_current)
                visited[next_current] = current


N, K = map(int, input().split())
visited = [-1] * 100001
path = []
bfs(N)
print(len(path) - 1)
print(*path[::-1])
