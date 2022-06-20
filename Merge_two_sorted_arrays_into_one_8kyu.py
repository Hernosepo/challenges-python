def merge_arrays(arr1, arr2):
    return [i for n, i in enumerate(sorted(arr1+arr2)) if i not in sorted(arr1+arr2)[:n]] 