def find_needle(haystack):
    for need in haystack:
        if need == "needle":
            need = haystack.index(need)
            need = "found the needle at position {}".format(need)
            return need
print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))


def find_needle(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))
