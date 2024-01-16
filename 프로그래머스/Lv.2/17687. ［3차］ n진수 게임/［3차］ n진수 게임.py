def convert(num, n):
    digit = "0123456789ABCDEF"
    res = ""
    if num == 0:
        return '0'
    while num > 0:
        num, mod = divmod(num, n) # 계속 나누고, 나머지 index는 결과에 넣어주기
        res += digit[mod]
    return res[::-1]
   
def solution(n, t, m, p):
    answer = ''
    s = ''
    # 최대 경우 문자열 생성
    for i in range(t * m):
        s += convert(i, n)
        
    # p 부터, m 순서로 t만큼
    p -= 1
    while len(answer) < t:
        answer += s[p]; p += m
    
    return answer