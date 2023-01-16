from collections import deque

N = int(input()) # pc 수
n = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(n):
    i,j = map(int, input().split())
    graph[i][j] = 1; graph[j][i] = 1

visited = [False for _ in range (N + 1)]
deq = deque([1])
visited[1] = True
count = 0


while deq:
    tmp = deq.pop()
    for i in range(1, N + 1):
        # 방문 x, 연결 ㅇ
        if visited[i] == False and graph[tmp][i] == 1:
            visited[i] = True
            deq.appendleft(i)
            count += 1
print(count)