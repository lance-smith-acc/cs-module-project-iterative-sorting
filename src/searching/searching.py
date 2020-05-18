def linear_search(arr, target):
    # Your code here
    # Loop through all elements in array
    for i in range(0, len(arr)):
    # Check if target matches element in array
        if arr[i] == target:
    # If element matches, return element
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # Seperate array into left and right sections
    left = 0
    right = len(arr) - 1

    # Loop until we have the answer
    while left <= right:
        # find the middle by adding the left and right and divide in half
        middle = (left + right) // 2

        # Check if we've found the answer
        if arr[middle] == target:
            return middle

        # Check if the target is higher or lower than middle
        # If the target is greater than the middle of the array, update the far left to equal the current middle + 1
        if arr[middle] < target:
            left = middle + 1
        # Otherwise, update the far right to equal the current middle - 1
        else:
            right = middle - 1


    return -1  # not found
