# returns the postion of x in the given array and if not found return -1
def binarySearch(arr, left_bound, right_bound, x):

    # Check base case
    if right_bound >= left_bound:

        middle = left_bound + (right_bound - left_bound) // 2

        # If element is present at the middle itself
        if arr[middle] == x:
            return middle

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[middle] > x:
            return binarySearch(arr, left_bound, middle-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, middle + 1, right_bound, x)

    else:
        # Element is not present in the array
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
