# Find the first non-consecutive number

def first_non_consecutive(arr):
    i = 1
    for x in arr:
        if i < len(arr) and arr[i] - arr[i-1] != 1:
            return arr[i]
        i += 1
    return None

print(first_non_consecutive([4,6,7,8,9,11]))