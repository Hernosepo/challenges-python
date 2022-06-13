def count(string):
    encarta = dict()
    for char in string:
        if char not in encarta:
            encarta[char] = 1
        else:
            encarta[char] = encarta[char] + 1

    return encarta


print(count("aba"))
    
