from heapq import heapify, heappop, heappush

def cookie(k, h):
    # convert list to heap
    heapify(h)
    ops = 0

    while True:
        f_min = heappop(h) # remove and return the first min element from heap

        if h:
            s_min = heappop(h) # remove and return the second min element from heap
            c = f_min + 2 * s_min
            heappush(h,c) #insert the element mentioned in its arguments into heap
            ops += 1
        else:
            return -1

# 8 90
# 13 47 74 12 89 74 18 38

if __name__ == "__main__":

    l1 = list(map(int, input().split()))
    h = list(map(int, input().split()))

    k = l1[1]
    
    print(cookie(k,h))
