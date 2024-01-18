def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board] # 문자열 list로 변환
    index_list = []
    
    while True:
        
        # 블록 확인 및 index 저장
        index_list.clear()
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                a = (i, j)
                b = (i, j + 1)
                c = (i + 1, j)
                d = (i + 1, j + 1)
                
                if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] == board[d[0]][d[1]] and board[a[0]][a[1]] != ' ':
                    index_list.append([a, b, c, d])
                    
        # index_list update
        for index in index_list:
            for i in index:
                board[i[0]][i[1]] = ' '
            
        # 아래로 내리기
        board = [list(item) for item in zip(*board)]
        
        for i in range(len(board)):
            board[i].sort(key = lambda x : x == ' ', reverse=True)
            
        board = [list(item) for item in zip(*board)]
                 
        # X 개수 check
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ' ':
                    count += 1
        # 종료 조건
        if answer == count:
            break
        else: answer = count
        
    return answer
