
s = list(input())
answer = ''
for c in s:
    if 'a' <= c <= 'z':
        c = ord(c) + 13
        if c > 122: c -= 26
        answer += chr(c)
    elif 'A'<= c <='Z':
        c=ord(c)+13
        if c>90: c-=26
        answer+=chr(c)
    else: answer+=c
print(answer)