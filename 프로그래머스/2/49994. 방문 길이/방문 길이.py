def solution(dirs):
    dir_dic = {'U':(0, 1), 'D':(0, -1), 'R': (1, 0), 'L': (-1, 0)}
    log = set() # 경로 저장 
    x, y = 0, 0 
    for dir in dirs:
        nx, ny = x + dir_dic[dir][0], y + dir_dic[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = (x, y, nx, ny)  
            reverse_path = (nx, ny, x, y)  # 반대 경로
            if path not in log and reverse_path not in log:
                log.add(path)
            x, y = nx, ny  # 위치 이동
    return len(log) # 이동 경로의 개수 반환
