def binarySearch(dataset, val):
    left = 0
    right = len(dataset) - 1
    while left <= right:
        mid = (left + right)//2
        if dataset[mid] != val:
            if dataset[mid] > val:
                right = mid -1
            if dataset[mid] < val:
                left = mid + 1
        else:
            return mid
    return -1