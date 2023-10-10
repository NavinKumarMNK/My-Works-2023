class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.map = [None for _ in range(self.size)]

    def _index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.map[idx]:
            self.map[idx] = ListNode(key, value)
            return
        current = self.map[idx]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next
    
    def get(self, key: int) -> int:
        idx = self._index(key)
        current = self.map[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        current = self.map[idx]
        last = None
        if not current:
            return
        while current:
            if current.key == key:
                if last == None:
                    self.map[idx] = current.next
                    return
                last.next = current.next
                del current
                return 

            last = current
            current = current.next
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
