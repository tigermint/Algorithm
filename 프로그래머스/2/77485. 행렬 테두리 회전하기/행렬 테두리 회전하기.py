from collections import deque

def rotate_clockwise(query):
    # 출발점
    rotate_list = [(query[0] - 1, query[1] - 1)] 
    
    for i in range(query[3] - query[1]):
        rotate_list.append((rotate_list[-1][0], rotate_list[-1][1] + 1))
        
    for i in range(query[2] - query[0]):
        rotate_list.append((rotate_list[-1][0] + 1, rotate_list[-1][1]))
                           
    for i in range(query[3] - query[1]):
        rotate_list.append((rotate_list[-1][0], rotate_list[-1][1] - 1))
        
    for i in range(query[2] - query[0] - 1):
        rotate_list.append((rotate_list[-1][0] - 1, rotate_list[-1][1]))
        
    # list 삽입
    deq = deque([matrix[rotate[0]][rotate[1]] for rotate in rotate_list])
    deq.appendleft(deq.pop())
    
    # 값 변환
    for i in range(len(deq)):
        matrix[rotate_list[i][0]][rotate_list[i][1]] = deq[i]
    return min(deq)

def solution(rows, columns, queries):
    global answer, matrix
    answer = []
    matrix = [[ i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        answer.append(rotate_clockwise(query))
    return answer