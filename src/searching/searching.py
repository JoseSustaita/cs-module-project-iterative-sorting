
def linear_search(arr, target):
    # Your code here
    iteration = -1
    for i in arr:
        iteration += 1
        # If present return location
        if i == target:
            return iteration
        # Otherwise not found
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1
    middle = 0
    while low <= high:
        middle = (low + high) // 2
        # If target<middle it can only be in left tree
        if target < arr[middle]:
            high = middle - 1  # Remove right
        # If target>middle it can only be in right tree
        elif target > arr[middle]:
            low = middle + 1  # Remove left
        else:
            return middle
    return -1  # not found
