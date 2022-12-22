def schedule(deadLine):
    J = [1]  # 1은 반드시 feasible함으로 추가
    for i in range(2, n + 1):  # 2부터 다른 배열에 J를 넣고
        K = insert(J, i, deadLine)  # 해당 i의 위치 찾으면서
        if is_feasible(K, deadLine):  # feasible한지, true라면 J에 삽입
            J = K[:]
    return J


def insert(J, i, deadLine):
    K = J[:]
    for j in range(len(J), 0, -1):
        if deadLine[i] >= deadLine[K[j - 1]]:
            j += 1 # 한칸 늘리기
            break
    K.insert(j - 1, i) # index K 배열에 맞게 넣기
    return K


def is_feasible(K, deadLine): # 적합성 확인
    for i in range(1, len(K) + 1): # 인덱스랑 보다 해당 원소 Deadline이 작아야 한다.
        if i > deadLine[K[i - 1]]:
            return False
    return True


# input
n = int(input()) # 작업의 개수

# 주의 -> 정렬되지 않은 상태라면 손으로 직접 정렬된 값을 input으로 넣어주자
# profit 내림차순이라 가정 -> 아니면 정렬해줘야 한다. , 각 작업에 다른 마감시간과 보상 
deadLine = list(map(int, input().split())) 
profit = list(map(int, input().split()))

# 작업 1부터 시작을 위해 가장 앞에 0을 삽입, 그럼 n + 1이 총 길이
deadLine.insert(0, 0) 
profit.insert(0, 0)

J = schedule(deadLine)

sumProfit = 0
profitList = []
deadLineList = []
for i in range(len(J)):
    sumProfit += profit[J[i]]
    deadLineList.append(deadLine[J[i]])
    profitList.append(profit[J[i]])

print(sumProfit)
print(*deadLineList)
print(*profitList, sep=" ") # *넣으면 리스트 출력시 대괄호 없어짐