import math
def solution(w,h):
    cnt = 0
    if w ==1 or h==1 :
        return 0
    if w == h : 
        return w*h-w
    for i in range(w) :
        cnt += (math.ceil(h*(i+1)/w) - math.floor(h*i/w))
    return w*h-cnt