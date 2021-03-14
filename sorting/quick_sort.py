# Complixty : O( N log N)
# Space: O(1)


def partition(array, start, end):
    pivot = array[start]
    i = start
    j = end

    while True:
        while i <= j and array[i] <= pivot:
            i = i + 1

        while i <= j and array[j] >= pivot:
            j = j - 1


        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[start], array[j] = array[j], array[start]

    return j


# def partition(arr, start, end):
#     # lec

#     pivot = arr[end]
#     i = start
#     for j in range(start, end):
#         if arr[j] <= pivot:
#             arr[i], arr[j], arr[j],arr[i]
#             i += 1
    
#     arr[i + 1], arr[end] = arr[end], arr[i + 1]
#     return i+1

def quick_sort(arr, l, r):
    if l < r:
        piv = partition(arr, l, r)
        quick_sort(arr, l, piv-1)
        quick_sort(arr, piv + 1, r)

if __name__ == "__main__":
    # arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    arr = [2,10,4,7,0]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

