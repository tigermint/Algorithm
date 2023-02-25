from itertools import permutations
def solution(k, dungeons):
    answer = -1
    permus = list(permutations(dungeons, len(dungeons)))
    
    for p_list in permus:
        tmp_k, count = k, 0
        for p in p_list:
            if tmp_k >= p[0]:
                tmp_k -= p[1]
                count += 1
            else: break
        if answer < count: answer = count 
        if answer == len(dungeons): break
            
    return answer