import math 
def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        answer += math.floor(math.sqrt(r2**2 - i**2)) - math.ceil(0 if i>r1 else math.sqrt(r1**2 - i**2)) + 1
    return answer*4