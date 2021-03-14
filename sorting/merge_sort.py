# the idea is
# The algorithm starts by splitting the original list of values in the middle to create
# two sublists, each containing approximately the same number of values
# After the list has been fully subdivided into individual sublists, the sublists are
# then merged back together, two at a time, to create a new sorted list. These sorted
# lists are themselves merged to create larger and larger lists until a single sorted
# list has been constructed. During the merging phase, each pair of sorted sublists
# are merged to create a new sorted list containing all of the elements from both
# sublists
# Complixty : O( N log N)
# Space: O(n)
# Stable
# N Extra memory location



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[0:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

if __name__ == "__main__":
    
    arr = [12, 11, 13, 5, 6, 7, 0, 19, 36, 5, -1]
    print("Given array is: ")
    print(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print(arr)