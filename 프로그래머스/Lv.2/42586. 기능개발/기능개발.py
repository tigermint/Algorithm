def cal(a, speed): # 배열 당 최소 배포 날짜
    count = 0
    while a < 100:
        a += speed
        count +=1
    return count
def solution(progresses, speeds):
    answer = []
    counts = []
    for i in range(len(progresses)):
        counts.append(cal(progresses[i], speeds[i]))  

    # 탐색하기
    index = 0 # answer 값에 넣을 인덱스
    answer.append(1)
    tmp = counts[0] # 더 큰지 확인
    for i in range(1, len(counts)):
        if(counts[i] > tmp):
            tmp = counts[i]
            index += 1
            answer.append(1)
        else:
            answer[index] += 1
        
    return answer