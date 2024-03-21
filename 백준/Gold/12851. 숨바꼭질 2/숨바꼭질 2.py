from collections import deque


def bfs(current):
    global result
    deq = deque([current])
    arr[current] = 0

    while deq:
        current = deq.popleft()
        if current == K:  # 발견
            result += 1
            continue

        for next_current in [current - 1, current + 1, current * 2]:
            if 0 <= next_current <= 100000 and (
                arr[next_current] == arr[current] + 1 or arr[next_current] == -1
            ):
                arr[next_current] = arr[current] + 1
                deq.append(next_current)


N, K = map(int, input().split())
arr = [-1] * 100001
result = 0
bfs(N)
print(arr[K])
print(result)
