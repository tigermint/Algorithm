from math import factorial
def solution(n, k):
    answer = []
    arr = [i + 1 for i in range(n)]

    while n != 0:
        fact = factorial(n - 1)
        # 몫 -> 그룹핑(arr 인덱스), 나머지 -> 다음 순회 k
        idx, k =  k // fact, k % fact
        if k == 0:
            answer.append(arr.pop(idx - 1))
        else:
            answer.append(arr.pop(idx))
        n -= 1
        
    return answer