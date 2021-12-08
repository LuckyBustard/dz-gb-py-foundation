words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_words = []

for word in words:
    if word[0] == '+' or word[0] == '-':
        sub_word = word[1::]
        if sub_word.isdigit():
            word = f"{word[0]}{int(sub_word):02d}"
            new_words.append('" ')
            new_words.append(word)
            new_words.append('"')
    elif word.isdigit():
        word = f"{int(word):02d}"
        new_words.append('" ')
        new_words.append(word)
        new_words.append('"')
    else:
        new_words.append(word + ' ')

new_words.reverse()
print("".join(new_words))
