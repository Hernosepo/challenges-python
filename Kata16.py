def tower_builder(n_floor):
    lst_tower = []
    pattern = '*'
    width = (n_floor * 2) - 1
    for items in range(1, 2 * n_floor, 2):
        asterisks = items * pattern
        ln = asterisks.center(width)
        lst_tower.append(ln)
    print(lst_tower)
    return lst_tower

tower_builder(1)# ['*', ])
#tower_builder(2)# [' * ', '***'])
#tower_builder(3)# ['  *  ', ' *** ', '*****'])
 
