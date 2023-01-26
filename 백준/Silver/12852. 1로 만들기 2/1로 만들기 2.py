from collections import deque
import sys
N = int(sys.stdin.readline())

deq = deque() # N을 1로 만드는 방법을 큐에 저장
deq.append([N])
visited = [0] * (N + 1)

while deq:
    node = deq.popleft()
    tmp = node[-1]
    if tmp == 1:
        break
    if not visited[tmp]:
        visited[tmp] = True
        if tmp % 3 == 0:
            deq.append(node + [tmp // 3])    
        if tmp % 2 == 0:
            deq.append(node + [tmp // 2])    
        deq.append(node + [tmp - 1])

print(len(node) - 1)
print(*node)