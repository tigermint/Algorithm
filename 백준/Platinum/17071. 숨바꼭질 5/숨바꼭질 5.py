from collections import deque

MAX_NUM = 500000
N, K = list(map(int, input().split()))

# visited[n][0] : 짝수 시간에 위치 n을 방문한 최소시간
# visited[n][1] : 홀수 시간에 위치 n을 방문한 최소시간
visited = [[-1 for _ in range(MAX_NUM + 1)] for _ in range(2)]


def bfs():
    deq = deque([[N, 0]])  # 수빈, time
    visited[0][N] = 0

    while deq:
        x, time = deq.popleft()
        flag = time % 2

        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 500000 and visited[1 - flag][nx] == -1:
                # nx 위치에는 time + 1 시간에 방문할 것이니까.
                # 그런데 time + 1 시간은 홀짝이 바뀌므로 1-flag로 해줌.
                visited[1 - flag][nx] = time + 1
                deq.append((nx, time + 1))


# 가능한 모든 점 방문
bfs()

# 방문한 다음에 K를 늘려보면서 이 점에 방문할 수 있는지 확인하기.
time, flag, result = 0, 0, -1
while K <= 500000:
    if visited[flag][K] != -1 and visited[flag][K] <= time:
        # time 이전에 수빈이가 K 위치에 방문했는지 확인
        result = time
        break
    flag = 1 - flag
    time += 1
    K += time

print(result)
