def positive_sum(arr):
    r = arr[:]
    for i in arr[:]:
        if i < 0:
            r.remove(i)
    return sum(r) , r
print(positive_sum([-1,-2,-3,-4,-5]))


# List comprehension

def positive_sum(arr):
    return sum(x for x in arr if x > 0)
