# returns the postion of x in the given array and if not found return -1
def binarySearch(arr, left_bound, right_bound, x):

    while left_bound <= right_bound:

        middle = left_bound + (right_bound - left_bound) // 2

        # Check if x is present at middle
        if arr[middle] == x:
            return middle

        # If x is greater, ignore left half
        elif arr[middle] < x:
            left_bound = middle + 1

        # If x is smaller, ignore right half
        else:
            right_bound = middle - 1

    # If we reach here, then the element was not present
    return -1


# test Code
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55

# call Function
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
