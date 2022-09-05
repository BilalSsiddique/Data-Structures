import time

def linearSearch(num, arr):
    for index in range(len(arr)):
        if arr[index] == num:
            return index
    return -1


num = 67
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


linSearch = linearSearch(num, arr)
if linSearch > -1:
    print(f"Number {num} found at {linSearch} index.")
else:
    print("Not found")
