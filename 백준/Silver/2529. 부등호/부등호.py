k = int(input())  # 숫자는 k + 1
inequality_signs = list(input().split())
nums = [True] * 10  # 0 ~ 9만 사용, 사용 check
min_num, max_num = "9999999999", "0"


def dfs(num, index):
    global min_num, max_num
    # 종료 조건
    if len(num) == k + 1:
        num_str = "".join(map(str, num))
        min_num = min(min_num, num_str)
        max_num = max(max_num, num_str)
        return

    # 실행 조건
    for i in range(10):
        if nums[i] and promising(index - 1, num[-1] if num else None, i):
            nums[i] = False
            num.append(i)
            dfs(num, index + 1)
            num.pop()
            nums[i] = True


def promising(index, x, y):
    if x is None or index < 0:
        return True
    if inequality_signs[index] == "<":
        return x < y
    elif inequality_signs[index] == ">":
        return x > y


dfs([], 0)
print(max_num)
print(min_num)