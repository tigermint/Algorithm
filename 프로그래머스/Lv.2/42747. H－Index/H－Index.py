def solution(citations):
    list = sorted(citations, reverse=True)  
    answer = 0
    i = list[0]
    while(1):
        if(i == 0):
            break
        count = 0
        for j in list: 
            if(i <= j): 
                count += 1
        if (i <= count): 
            answer = i
            break 
        i-=1
    return answer