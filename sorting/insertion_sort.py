# Complextiy: O(n^2)
# Space Complextiy : O(1)
# num of comparisons : n^2 --> N = 6 , comp = 36
#  Num of swaps : n^2  --> N = 6, swap = 36
# stable 
# One extram temp variable

arr = [10, 15, 70, 12, 20, 80]

for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print(arr)
