# 기존 방식대로 재귀를 거쳐서 promising을 할 시 효율성 낭비가 생긴다
# 따라서 먼저 promising을 통해 확인한 뒤 해당하는 노드만 다음 노드의 재귀문으로 들어간다.
def n_queens(i, cols): # i : 현재 row 
    global n, Max, count
    for col in range(1, n + 1): # 다음 row의 col 탐색 -> 먼저 확인하고 맞을 시 다음 재귀로 넘어간다.
        cols[i + 1] = col
        if promising(i + 1, cols): # 다음 row가 올바른지
            if i + 1 == n:
                result = int("".join(map(str, cols[1:n+1])))
                count += 1
                Max = max(Max, result)
            else:
                n_queens(i + 1, cols)
       
    

def promising(i, cols):
    k = 1
    flag = True
    # 지금까지의 col들과 모두 확인한다.
    while k < i and flag:
        if cols[k] == cols[i] or ((i - k) == abs(cols[i] - cols[k])): 
            flag = False
        k += 1
    return flag

n = int(input())
Max = 0
count = 0
cols = [0 for _ in range(n + 1)] # col 1 2 3 4 -> col 만 확인하면 되기 때문에
n_queens(0, cols)
print(str(count) + "\n" + str(Max))


