def solution(s):
    answer = len(s)
    unit = int(len(s) / 2)

    for u in range(unit, 0, -1):
        start, end = 0, u
        tmp_answer = 0
        repeat = 1  # 동일한 문자열 반복 횟수
        while end <= len(s):
            if s[start:start + u] == s[end:end + u]:
                repeat += 1
                end += u
            else:
                tmp_answer += len(s[start:start + u]) if repeat == 1 else len(str(repeat)) + u
                repeat = 1
                start = end
                end = start + u
        tmp_answer += len(s) - start
        answer = min(tmp_answer, answer)
    return answer
