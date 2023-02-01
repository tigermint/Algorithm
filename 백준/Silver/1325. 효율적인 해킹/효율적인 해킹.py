import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

# 메모리 축소를 위해 인접 리스트로
for _ in range(M):
    a, b = map(int, input().split())
    graph[b-1].append(a-1)  # a가 b를 신뢰한다 b -> a


def bfs(start):
    deq = deque([start])
    visited = [0] * N
    visited[start] = 1
    while deq:
        tmp = deq.popleft()
        for i in graph[tmp]:
            if not visited[i]:
                deq.append(i)
                visited[i] = 1
    return sum(visited)


hack = [0] * N
for i in range(N):
    hack[i] = bfs(i)

max_value = max(hack)
for i in range(N):
    if hack[i] == max_value:
        print(i + 1, end=" ")
