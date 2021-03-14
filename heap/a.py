def rotate_left(d, arr):
    l = arr[:d]
    return arr[d:] + l

if __name__ == "__main__":
    a = [1,2,3,4,5]

    print(rotate_left(3,a))