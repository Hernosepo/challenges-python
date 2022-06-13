def to_freud(sentence):
    list_of_words = []
    for word in sentence:
        list_of_words = sentence.split()
        for i in range(len(list_of_words)):
            if list_of_words[i] != word:
                list_of_words[i] = "sex"
        return " ".join(list_of_words)


print(to_freud("You're becoming a true freudian expert")) 
