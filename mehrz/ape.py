n = 256 
c = 1
while n != 1:
    if c % 2 == 0:
        n = n/2
    else:
        n = n/4

    c +=1

print(c, n)
