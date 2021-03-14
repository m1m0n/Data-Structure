eqn = "6/2-3+4*2" # 2 3 4 * +
stack = []
l = 0
for i in eqn:
    if i in ['+', '-', "*", '/']:
        stack.append(i)
        l += 1
    else:
        print(i, end=" ")

for i in range(l):
    print(stack.pop(), end=" ")