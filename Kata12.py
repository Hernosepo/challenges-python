def unique_in_order(iterable):
    lst =[]
    yasta = None
    for x in iterable[0:]:
        if x != yasta:
            lst.append(x)
            yasta = x
    return lst


print(unique_in_order("AAAABBBCCDAABBB"))
 
