# Linear Probing: best cache performance but a lot of clustring
# Double hashing: less cache performance but not clustring
# Quadratic : between them
class MyHashTable:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return str(self.slots )

    def __len__(self):
        count = 0
        for i in self.slots:
            if i != None:
                count += 1
        return count

    def hash1(self, key):
        i = key % self.size
        return i
    
    def hash2(self, key):
        i = 1 + key % 8 # prime number
        return i

    def insert(self, key):
        slot = self.hash1(key)
        while True:
            if self.slots[slot] is None or self.slots[slot] == -2:
                self.slots[slot] = key
                return slot
            else:
                slot = (slot + 1) % self.size # liner probing

    def search(self, search_key):
        slot = self.hash1(search_key)
        if self.slots[slot] is None:
            return -1
        for i in range(self.size):
            mod = (slot + i) % self.size # linear probing
            if self.slots[mod] == search_key:
                return mod
                
        return -1
    
    def delete(self, delet_key):
        slot = self.hash1(delet_key)
        for i in range(self.size):
            if self.slots[slot] is None or self.slots[slot] == -2:
                pass
            else:
                mod = (slot + i) % self.size
                if self.slots[mod] == delet_key:
                    self.slots[mod] = -2 # delete
                    return
                else:
                    pass

if __name__ == "__main__":
    m = MyHashTable(5)

    m.insert(13) # 13 % 5 = 3
    m.insert(83) # 83 % 5 = 3
    m.insert(93) # 93 % 5 = 3
    m.insert(52) # 52 % 5 = 2
    print(m)
    m.delete(83)
    print(m)
    # print(m.search(13)) # 3
    # print(m.search(70)) # -1
    print(m.search(3)) # -1
    # print(m.search(2)) # -1
    m.insert(53)
    print(m)