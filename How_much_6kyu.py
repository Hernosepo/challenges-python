
def howmuch(m, n):
    infimus = min(m, n) #min
    maximus = max(m, n) #max
    lst = []
    while (infimus <= maximus): #keep is going while
        if ((infimus % 9 == 1) and (infimus %7 == 2)):
            lst.append(["M: " + str(infimus), "B: " + str(infimus // 7), "C: " + str(infimus // 9)])
        infimus += 1
    return lst
