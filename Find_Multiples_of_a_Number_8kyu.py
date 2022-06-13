def find_multiples(integer, limit):
    multiplos = []
    for num in range(integer, limit + 1):
        if num%integer == integer%integer:
            multiplos.append(num)
    return multiplos
print(find_multiples(1, 2))
