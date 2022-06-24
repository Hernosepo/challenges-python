# Descending Order

def descending_order(num):
    digits = sorted([int(a) for a in str(num)], reverse= True)
    return int("".join(map(str, digits)))

print(descending_order(5432167))