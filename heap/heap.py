class Heap:
    def __init__(self, max_size):
        self.elements = [None] * max_size
        self.count = 0
    
    def __len__(self):
        return self.count
    
    def capacity(self):
        return len(self.elements)
    
    def print_heap(self):
        for i in range(self.count):
            print(self.elements[i], end=" ")
        

    def add(self, val):
        self.elements[self.count] = val
        self.count += 1
        self.heap_up(self.count - 1) # cuz it is an array zero based

    
    def heap_up(self, index):
        if index > 0:
            parent = index // 2
            # for max heap use >
            if self.elements[index] < self.elements[parent]:
                self.elements[index], self.elements[parent] = self.elements[parent], self.elements[index]
                self.heap_up(parent)
                
    def remove(self):
        val = self.elements[0]
        self.count -= 1
        self.elements[0] = self.elements[self.count]
        self.heap_down(0)
        return val

    def heap_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2

        large = index                               # for max heap >=    
        if left < self.count and self.elements[left] >= self.elements[large]:
            large = left
        elif right < self.count and self.elements[right] >= self.elements[large]:
            large = right
        
        if large != index:
            self.elements[index], self.elements[large] = self.elements[large], self.elements[index]
            self.heap_down(large)

def heap_sort(arr):
    n = len(arr)
    for i in range(n):
        arr.heap_up(i)

    for j in range(n-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        arr.heap_down(j)

if __name__ == "__main__":
    h = Heap(5)
    h.add(6)
    h.add(8)
    h.add(10)
    h.add(9)
    h.add(11)


    h.print_heap()
    print()
    # print(h.remove())
    # h.print_heap()
    # # print()
    # # print(h.remove())
    # # print(h.remove())
    # # print(h.remove())

    for i in range(5):
        print(h.remove())