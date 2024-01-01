from collections import deque
dic = {
    '}': '{',
    ']': '[',
    ')': '('
}
def check(deq):
    stack = []
    for item in deq:
        if not stack:
            stack.append(item)
        elif item not in dic:
            stack.append(item)
        else:
            stack.pop() if dic[item] == stack[-1] else stack.append(item)
    return not stack

def solution(s):
    answer = 0
    deq = deque(s)
    for _ in range(0, len(deq)):
        deq.append(deq.popleft())
        if check(deq): answer += 1 
    return answer