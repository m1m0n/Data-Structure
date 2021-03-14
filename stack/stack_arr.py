def decimal_to_b(n, b):
    stack = []
    while n > 0:
        tmp = str(hex(n % b)[2:])
        stack.append(tmp)
        n = abs(n / b)

    return "".join(stack[::-1])


if __name__ == "__main__":
    stack = []
    print(stack)  # []
    stack.append('A')
    print(stack)  # [A]
    stack.append('B')
    print(stack)  # [A,B]
    val = stack.pop()
    print(val)  # B
    val = stack.pop()
    print(val)  # A

    # print(stack.top())  # None

    # n = 92

    # print(decimal_to_b(n,16))
