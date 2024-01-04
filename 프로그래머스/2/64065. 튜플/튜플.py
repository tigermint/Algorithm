def solution(s):
    answer = []
    s_list = [list(map(int, item.split(','))) for item in s[2:-2].split('},{')]
    s_list.sort(key=len)
    
    for s_item in s_list:
        answer += list(set(s_item) - set(answer))

    return answer
