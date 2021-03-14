import sys

def find_min(A, n):
    if n == 1:
        return A[0]
    return min(A[n-1], find_min(A, n-1))


def check(s):
    stack = list(s)
    tmp = stack.pop(0)
    if tmp == stack.pop():
        pass
    else:
        return False
    return True


if __name__ == "__main__":
    A = [1, 4, 45, 6, -50, 10, 2]
    s = "boob"
    print(check(s))
    print(sys.version)
    # print(find_min(A, len(A)))
