class MyHashMap:
    def __init__(self):
        self.hashtable = {}

    def put(self, key: int, value: int) -> None:
        self.hashtable[key] = value

    def get(self, key: int) -> int:
        return self.hashtable[key] if key in self.hashtable else -1

    def remove(self, key: int) -> None:
        if key in self.hashtable:
            del self.hashtable[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
