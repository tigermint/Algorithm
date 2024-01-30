from string import ascii_lowercase
dic = dict()
word = input()
for i in list(ascii_lowercase):
    dic[i] = 0
for w in word:
    dic[w] += 1
for i in dic.values():
    print(i, end = ' ')
print()
