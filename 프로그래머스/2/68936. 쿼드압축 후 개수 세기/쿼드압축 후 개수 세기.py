def check(arr): # 모두 같은지 확인
    number = arr[0][0]
    for i in arr: # row
        for j in i: # row의 column
            if number != j: 
                return False
    return True

def solution(arr):
    n = len(arr)

    # 종료 조건
    # 한 칸이 남았거나, 전체가 모두 같거나
    if n==1 or check(arr):
        if arr[0][0] == 0:
            return 1,0
        return 0,1
    
    # recur, 4등분
    z1,o1 = solution([i[:n//2] for i in arr[:n//2]]) # 1번
    z2,o2 = solution([i[n//2:] for i in arr[:n//2]]) # 2번
    z3,o3 = solution([i[:n//2] for i in arr[n//2:]]) # 3번
    z4,o4 = solution([i[n//2:] for i in arr[n//2:]]) # 4번

    return [z1+z2+z3+z4,o1+o2+o3+o4]