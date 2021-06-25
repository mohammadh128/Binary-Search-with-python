# Binary-Search-with-python
Python Program for Binary Search (Recursive and Iterative)

Given a sorted array arr of n elements, we write a function to search a given element x in arr[].
Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

---------------------------------
step 1:
  Compare x with the middle element.

---------------------------------
step 2:
  If x matches with the middle element, we return the middle index.
  
---------------------------------
step 3:
  Else If x is greater than the middle element, then x is in the right half. So we recur for the right half.
  
---------------------------------
step 4:
  Else (x is smaller) recur for the left half.
  
