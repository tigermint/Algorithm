def nQueens(i, col):
    global count
    global max
    n = len(col) - 1
    if promising(i, col): # 다음 level로 가서 검사한다, prunning 되었을 경우 다시 돌아간다. 만약 SST 그리라고 하면 접근 여부 생각하기
        if i == n: 
            count += 1
            print("경로: " + str(col[1: n + 1]))   
            num = int(''.join(map(str, col[1:n + 1])))
            if max < num:
                max = num
            
        else:
            for j in range(1, n + 1): 
                col[i + 1] = j
                nQueens(i + 1, col)

def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k): # col값이 같거나 대각선 값이 같으면 pruning
            flag = False 
        k += 1
    return flag

count = 0 # 가능한 체스보드 수
n = int(input()) # n * n 체스보드 판

# 만약 n * m인 경우 -> 더 큰걸 n으로 생각해서 넣고 맞게 배제시키면 된다.
# n > m인 경우 ... n - m만큼 뒤에서 자르기
# n < m인 경우 ... n보다 큰 값이 경로에 있으면 배제시키기

col = [0] * (n + 1) # col의 위치 인덱싱 할 리스트, 인덱스랑 동일시 하기 위해 맨 앞 0, 0 1 3 2 4 이런 식
max = 0 # 경로 숫자로 변환 했을 경우 가장 큰 값

nQueens(0, col)

print(count)
print(max)


