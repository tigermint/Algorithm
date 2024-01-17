def solution(msg):
    answer = []
    dic = {}
    check = 27
    # 사전 초기화
    for num in range(0, 26):
        alpha = chr(num + 65)
        dic[alpha] = num + 1

    start = 0
    value = 27
    while start < len(msg):
        # dic에 있는 가장 긴 문자열 찾기
        for i in range(len(msg), start, -1): # 문자열의 뒤에서부터 탐색
            if msg[start:i] in dic.keys(): 
                answer.append(dic[msg[start:i]])
                # dic에 새로운 문자열 추가
                if i<len(msg): 
                    dic[msg[start:i+1]] = value
                    value += 1
                start = i
                break

    return answer
