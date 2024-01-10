def solution(record):
    answer = []
    dic = {}
    for r in record: 
        r_list = r.split(' ')
        if r_list[0] != 'Leave':
            dic[r_list[1]] = r_list[2]
    
    for r in record:
        r_list = r.split(' ')
        if r_list[0] == 'Enter':
            answer.append(dic[r_list[1]] + '님이 들어왔습니다.')
        elif r_list[0] == 'Leave':
            answer.append(dic[r_list[1]] + '님이 나갔습니다.')
        
    return answer