# 1
# 2  9
# 3 10  8
# 4  5  6  7
# 일직선으로: 0
# ->: 1
# 위쪽 + 왼쪽 : 2
# n번 만큼 반복

def solution(n):
    answer = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]
    
    x, y = -1, 0
    number = 1
    for i in range(n): # 방향 0, 1, 2
        for _ in range(i, n): # 좌표 0 ~ 5이면 5개 변 만들어짐
            if i % 3 == 0: x += 1 # 0번째 - 위 ~ 아래
            elif i % 3 == 1: y += 1 # 1번째 - 왼 ~ 오
            else: x -= 1; y -= 1 # 2번쨰 - 대각선 왼쪽 방향
            answer[x][y] = number
            number += 1
    return sum(answer, []) 
# sum() 하면 0 + [1, 2] + [1, 2, 3]이라 에러
# sum(a, []) 하면 [] + [1, 2] + [1, 2, 3] 리스트 합치기
