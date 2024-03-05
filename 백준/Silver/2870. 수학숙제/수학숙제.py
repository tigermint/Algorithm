import re

M = int(input())
numbers = []
for _ in range(M):
    for num in list(map(int, re.findall(r"\d+", input()))):
        numbers.append(num)
print(*sorted(numbers), sep="\n")
