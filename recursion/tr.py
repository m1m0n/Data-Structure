def triangle(n):
    if n == 1:
        return 1
    else:
        return n + triangle(n-1)

def triangle2(n):
    # T = n * (n+1)/2
    t = 0
    for i in range(n):
        t += i*(i+1)/2
    
    return t

if __name__ == "__main__":
    print(triangle(4))
    print(triangle2(4))