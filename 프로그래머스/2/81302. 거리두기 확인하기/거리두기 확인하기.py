def bfs(x,y,k):
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    
    for k1 in range(4): # 상하좌우 check
        subx = x + dx[k1]
        suby = y + dy[k1]
        
        if subx < 0 or subx >= 5 or suby < 0 or suby >= 5: continue # 끝자리인지 check
        if k[subx][suby] == 'P': return False # 바로 옆자리 P면 false
        
        if k[subx][suby] == 'O': # 바로 옆자리 비어있을 경우
            for k2 in range(4): # 맨해튼 거리 측정
                subx2 = subx + dx[k2]
                suby2 = suby + dy[k2]
                if subx2 < 0 or subx2 >= 5 or suby2 < 0 or suby2 >= 5:
                    continue
                if subx2 == x and suby2 == y:
                    continue
                if k[subx2][suby2] == 'P':
                    return False
    return True
        
    
def solution(places):
    answer = []
    for k in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if k[i][j] == 'P':
                    if not bfs(i,j,k):
                        answer.append(0)
                        flag = 0
                        break
            if flag == 0:
                break
        if flag == 1:
            answer.append(1)
                      
    return answer