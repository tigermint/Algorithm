import re
from itertools import permutations

def  solution(expression):
    # 분리
    operators = [i for i in expression if not i.isdigit()]
    numbers = re.split('[\+\-\*]', expression)
    
    # operators 조합 뽑기
    per = permutations(list(set(operators)))
    answer = []
    for p in per:
        operator = operators[:]
        number = numbers[:]
        
        # 연산
        for i in p:
            idx = 0
            while idx < len(operator):
                k = operator[idx]
                if i == k:
                    operator.pop(idx)
                    if k == '+':
                        number[idx] = str(int(number[idx]) + int(number.pop(idx+1)))
                    elif k == '-':
                        number[idx] = str(int(number[idx]) - int(number.pop(idx+1)))
                    else:
                        number[idx] = str(int(number[idx]) * int(number.pop(idx+1)))
                else:
                    idx += 1
        answer.append(abs(int(number[0])))
    return max(answer)