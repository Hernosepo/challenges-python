def abbrev_name(name):
    for nd in name:
        nd = name.split(" ")
        ndf = "{}.{}".format(nd[0][0],nd[1][0])
    return ndf.upper()


print(abbrev_name("patrick feenan"))
 
