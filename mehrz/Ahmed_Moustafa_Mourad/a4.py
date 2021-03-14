# I think that the required is to remove duplicates elements from the array
# so I implemented it as following

arr1 = [10, 15, 70, 12, 20,70 ,80, 15, 10]
arr1 = list(set(arr1))

for i in range(1, len(arr1)):
    key = arr1[i]
    j = i
    while j > 0 and key <= arr1[j - 1]:
        arr1[j] = arr1[j-1]
        j -= 1
    arr1[j] = key

print(35*"=")
print("First Approach")
print(arr1)

# After a little bit of searching I found this approach of the implementation
# When a duplicate is found, write over one of the duplicated items
# with a key value less than any normally used (such as –1, if all the normal keys
# are positive). Then the normal insertion sort algorithm, treating this new key
# like any other item, will put it at index 0. From now on the algorithm can
# ignore this item. The next duplicate will go at index 1, and so on. When the
# sort is finished, all the removed dups (now represented by –1 values) will be
# found at the beginning of the array. The array can then be resized and shifted
# down so it starts at 0.


arr = [10, 15, 70, 12, 20,70 ,80, 15, 10]

for i in range(1, len(arr)):
    key = arr[i]
    j = i
    while j > 0 and key <= arr[j - 1]:
        if key == arr[j - 1]:
            key = -1
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = key
print(35*"=")
print("Second Approach")
print(arr)
