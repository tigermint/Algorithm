def solution(s):
    answer = [0, 0]
    while s != "1":
        before_len = len(s)
        after_len = len(list(filter(lambda a : a == '1', s)))
        s = format(after_len, 'b')
        answer[0] += 1; answer[1] += (before_len - after_len)
    return answer
        
