#Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted
#string, the longest possible, containing distinct letters - each taken only once -
#coming from s1 or s2.
# Tengo 2 strings, tengo que imprimir 1 string donde se encuentren todas las letras
# sin repetirlas y puede salir ordenado
def longest(a1, a2):
    dict = []
    a3 = a1 + a2
    for orig in a3:
        if orig not in dict:
            dict.append(orig)
    return "".join(sorted(dict))

print(longest("loopingisfunbutdangerous","lessdangerousthancoding"))


# abcdefghilnoprstu
