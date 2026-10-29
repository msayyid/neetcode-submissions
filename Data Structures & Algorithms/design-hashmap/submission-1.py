class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.my_map = [None] * 1000 

    def _hash(self, key):
        return key % 1000
        

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        current = self.my_map[index] # current is now the head
        if current is None:
            self.my_map[index] = Node(key, value)
        else:
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    current.next = Node(key, value)
                    return
                current = current.next


    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.my_map[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        prev = None
        current = self.my_map[index]
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.my_map[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)