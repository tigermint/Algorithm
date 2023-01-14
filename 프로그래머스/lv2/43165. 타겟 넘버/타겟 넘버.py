
def solution(numbers, target):
    answer = 0
    def dfs(nums_sum, index):
        if index == len(numbers):
            if nums_sum == target:
                nonlocal answer
                answer += 1
            return
        dfs(nums_sum + numbers[index], index + 1)
        dfs(nums_sum - numbers[index], index + 1)
    dfs(0, 0)
    return answer