# Find the first non-consecutive number

def first_non_consecutive(arr):
    x = [arr[n+1] for n in range(len(arr)-1) if arr[n+1] - arr[n] != 1]
    return int(x)


print(first_non_consecutive([4,5,6,7,8,9,11]))