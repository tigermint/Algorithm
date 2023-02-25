def solution(numbers):
    sorted_nums = list(map(str, sorted(numbers, key = lambda x : str(x)*3, reverse = True)))
    return "0" if sorted_nums[0] == "0" else ''.join(sorted_nums)