# Iterative binary_search

def binarySearch(number, arr):
    min = 0
    max = len(arr)-1
    
    while min <= max:
        mid = (min+max)//2
        if arr[mid] < number:
            min = mid+1
        elif arr[mid] > number:
            max = mid-1
        else:
            return mid

    return -1


num = 42
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

binSearch = binarySearch(num, arr)
if binSearch > -1:
    print(f"Number {num} found at {binSearch} index.")
else:
    print("Not found")
    