from collections import deque

def solution(n, computers):
    answer  = 1
    queue = deque([0])
    visited = [0] * n
    visited[0] = 1
    
    while 0 in visited:
        node = queue.popleft()
        for idx in range(len(computers[node])):
            if computers[node][idx] == 1 and visited[idx] == 0: 
                queue.append(idx)  
                visited[idx] = 1
        # 네트워크 종료 check
        if len(queue) == 0:
            answer += 1
            for i in range(len(visited)):
                if visited[i] == 0:
                    queue.append(i)
                    break
    return answer
            
        
            
            
            
    
    
