import sys

input = sys.stdin.readline

K = int(input())
nums = list(map(int, input().split()))
tree = [0 for _ in range(2**K)]


def make_tree(nums, start, end, root):
    if start > end:
        return
    mid = (start + end) // 2
    tree[root] = nums[mid]
    make_tree(nums, start, mid - 1, 2 * root)
    make_tree(nums, mid + 1, end, 2 * root + 1)


make_tree(nums, 0, len(nums) - 1, 1)

i = 1
while i < 2**K:
    for j in range(i, i * 2):
        print(tree[j], end=" ")
    print()
    i *= 2
