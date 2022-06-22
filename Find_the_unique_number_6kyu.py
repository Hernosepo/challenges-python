# Find the unique number

def find_uniq(arr):
    ordenada = sorted(arr)
    ordenada_rev = sorted(arr, reverse=True)
    if ordenada[0] is not ordenada[1]:
        return ordenada[0]
    elif ordenada_rev[0] is not ordenada_rev[-1]:
            return ordenada_rev[0]





print(find_uniq([1, 1, 1, 3, 1, 1]))