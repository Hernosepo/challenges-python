def bouncing_ball(h, bounce, window):
    if h < 0 or bounce > 1 or bounce < 0 or window > h:
        return -1
    else:
        count = 1
        h = h * bounce
        while h > window:
            h = h * bounce
            count = count + 2
    return count

print(bouncing_ball(-1,-1,0))


 
#def bouncing_ball(h, bounce, window):
#    bounces = 0
#    if (bounce >= 1) or (bounce <=0) or (h <0) or (window<0) or (window==h):
#        return -1
#    while h > window:
#        h = bounce*h
#            bounces += 2
#    return bounces + 1
