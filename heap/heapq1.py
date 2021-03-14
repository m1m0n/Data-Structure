from heapq import heapify, heappop, heappush, nsmallest

if __name__ == "__main__":

    heap = []
    up = set()

    for i in range(int(input())):
        t = list(map(int, input().split()))

        if t[0] == 1:
            heappush(heap, t[1])
            up.add(t[1])

        elif t[0] == 2:
            # heappop(heap)
            up.discard(t[1])

        else:
            while heap[0] not in up:
                heappop(heap)
            
            print(heap[0])