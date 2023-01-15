from collections import deque
def solution(maps):
    answer = -1
    max_row = len(maps); max_col = len(maps[0])
    visited = [[False] * max_col for _ in range(max_row)]
    deq = deque([(0, 0)])
    visited[0][0] = 1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북
    
    # BFS
    while deq:
        node = deq.popleft()
        # 종료
        if node[0] == max_row - 1 and node[1] == max_col - 1:
            return visited[node[0]][node[1]]
        for direction in directions:
            tmp_node = (node[0] + direction[0], node[1] + direction[1])
        
            # 범위 벗어남
            if tmp_node[0] < 0 or tmp_node[1] < 0 or tmp_node[0] >= max_row or tmp_node[1] >= max_col:
                pass
            # 이미 방문 or 방문 못함
            elif visited[tmp_node[0]][tmp_node[1]] or maps[tmp_node[0]][tmp_node[1]] == 0:
                pass
            # 방문
            else:
                visited[tmp_node[0]][tmp_node[1]] = visited[node[0]][node[1]] + 1
                deq.append(tmp_node)   
    return answer