

def binarySearch(num, arr, min, max):
    if max >= min:

        mid = (min+max) // 2

        if arr[mid] == num:
            return mid

        elif arr[mid] > num:
            return binarySearch(num, arr, min, mid-1)

        else:
            return binarySearch(num, arr, mid+1, max)

    return -1


num = 46
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

binSearch = binarySearch(num, arr, 0, len(arr)-1)
if binSearch != - 1:
    print(f"Number {num} found at {binSearch} index.")
else:
    print("Not found")
