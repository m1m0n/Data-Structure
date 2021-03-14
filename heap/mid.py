from heapq import heapify, heappop, heappush, nsmallest

def midian(a):
    l = []
    for i in range(int(input())):
        l.append(int(input()))
        l.sort()
        mid = 0
        if len(l) % 2 == 0: # even length
            mid = (l[len(l)//2] + l[len(l)//2-1])/2
            print("%.1f" % mid)
        elif len(l) % 2 != 0: # odd length
            mid = (l[len(l)//2])
            print("%.1f" % mid)

def heap_sort(i):
    h = []
    for value in i:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


if __name__ == "__main__":
    
    # midian(6)

    l = []
    for i in range(int(input())):
        # l.append(int(input()))
        heappush(l, int(input()))
        heapify(l)
        heap_sort(l)
        if len(l) % 2 == 0: # even length
            mid = (l[len(l)//2] + l[len(l)//2-1])/2
            print(l)
            print("%.1f" % mid)
        elif len(l) % 2 != 0: # odd length
            mid = l[len(l)//2]
            print(l)
            print("%.1f" % mid)