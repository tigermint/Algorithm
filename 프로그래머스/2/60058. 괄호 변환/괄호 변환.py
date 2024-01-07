def correct_parenthesis(string): 
    stack = []
    for s in string:
        if not stack: 
            stack.append(s)
        elif stack[-1] == '(' and s == ')':
            stack.pop()
        else: stack.append(s)
    return True if not stack else False

def balanced_paraenthesis(string):
    stack = []
    for s in string:
        if not stack:
            stack.append(s)
        elif (stack[-1] == '(' and s == ')') or (stack[-1] == ')' and s == '('):
            stack.pop()
        else: stack.append(s)
    return True if not stack else False

def seperate_uv(string):
    u, v = [], []
    check_idx = 0
    for idx in range(0, len(string)):
        u.append(string[idx])
        if balanced_paraenthesis(u):
            check_idx = idx; break
    for idx in range(check_idx+1, len(string)):
        v.append(string[idx])
    return u, v

def trans(p):
    if p == '': return p
    u, v = seperate_uv(p)
    if correct_parenthesis(''.join(u)):
        return ''.join(u) + trans(''.join(v))
    else:
        new_u = []
        for idx in range(1, len(u)-1):
            if u[idx] == '(': new_u.append(')')
            else: new_u.append('(')
        return '(' + trans(''.join(v)) + ')' + ''.join(new_u)

def solution(p):
    if correct_parenthesis(p): return p
    else:
        return trans(p)
