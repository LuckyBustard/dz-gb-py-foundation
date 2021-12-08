words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(words):
    if words[i][:1] == '+' or words[i][:1] == '-':
        sub_word = words[i][1::].strip()
        if sub_word.isdigit():
            words[i] = f"{words[i][0]}{int(sub_word):02d}"
            words.insert(i, '" ')
            i += 2
            words.insert(i, '"')
    elif words[i].strip().isdigit():
            words[i] = f"{int(words[i]):02d}"
            words.insert(i, '" ')
            i += 2
            words.insert(i, '"')
    else:
        words[i] += ' '
    i += 1

words.reverse()
print("".join(words))
