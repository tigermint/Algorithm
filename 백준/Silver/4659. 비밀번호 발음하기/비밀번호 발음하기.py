while True:
    password = input()
    if password == "end":
        break
    flag = True
    vowels = "aeiou"

    vowel_count = 0
    vowel_repeat, consonant_repeat = 0, 0
    tmp = ""

    for p in password:
        if p in vowels:  # 모음인 경우
            consonant_repeat = 0
            vowel_count += 1
            vowel_repeat += 1
            if vowel_repeat >= 3:
                flag = False
            if tmp == p:
                if p == "e" or p == "o":
                    pass
                else:
                    flag = False
        else:  # 자음인 경우
            vowel_repeat = 0
            consonant_repeat += 1
            if consonant_repeat >= 3:
                flag = False
            if tmp == p:
                flag = False
        tmp = p

    if vowel_count < 1:
        flag = False

    if flag:
        print("<%s> is acceptable." % password)
    else:
        print("<%s> is not acceptable." % password)