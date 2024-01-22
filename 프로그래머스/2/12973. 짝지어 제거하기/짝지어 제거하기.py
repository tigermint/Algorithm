def solution(s):   
    s = list(s)
    data = [s[0]]
    for i in range(1, len(s)):
        if(len(data) != 0 and data[-1] == s[i]):
            data.pop()
        else: data.append(s[i])
        
    return 1 if len(data) == 0 else 0