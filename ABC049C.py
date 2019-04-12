word = input()
result = ""
words = ["dream", "dreamer", "erase", "eraser"]
len_word = len(word)
tmp = word

while tmp != "":
    tmp_words = []
    #print(tmp, result)
    for i in words:
        if tmp.startswith(i):
            tmp_words.append(i)
    # print(tmp_words)
    chosen_word = ""
    for j in tmp_words:
        check_word = tmp.replace(j, "", 1).strip()
        # print(check_word)
        if j == tmp:
            result += j
            tmp = tmp.lstrip(j)
            break
        for k in words:
            if check_word.startswith(k):
                chosen_word = j
    # print(chosen_word)
    if chosen_word == "":
        break
    result += chosen_word
    tmp = tmp.replace(chosen_word, "", 1).strip()


if result == word:
    print("YES")
else:
    print("NO")
