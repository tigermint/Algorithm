word = input()
print(1 if ''.join(reversed(word)) == word else 0)