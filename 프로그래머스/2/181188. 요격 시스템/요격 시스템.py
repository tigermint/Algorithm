def solution(targets):
    answer, end = 0, 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    for target in targets:
        if target[0] >= end:
            answer += 1
            end = target[1]
    
    return answer