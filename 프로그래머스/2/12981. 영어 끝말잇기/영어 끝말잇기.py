# 가장 먼저 탈락하는 사람 번호, 몇 번째 차례 탈락
# 마지막 글자도 확인해야함
import math
def solution(n, words):
    logs = []
    for i in range(len(words)):
        if words[i] in logs or (i != 0 and words[i - 1][-1] != words[i][0]):
            return [i % n + 1, math.ceil((i + 1) / n)]
        else: logs.append(words[i])
    return [0, 0]