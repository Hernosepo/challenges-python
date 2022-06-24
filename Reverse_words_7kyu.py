# Reverse words

def reverse_words(text):
    str_lst = []
    for word in text.split(' '):
        str_lst.append(word[::-1])
    return ' '.join(str_lst)

print(reverse_words('double  spaced  words'))