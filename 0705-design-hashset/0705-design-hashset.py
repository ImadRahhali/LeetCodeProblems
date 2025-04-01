class MyHashSet:

    def __init__(self):
        self.table = []
    def add(self, key: int) -> None:
        code = hash(key)
        t = self.table
        if code not in self.table:
            t.append(code)
    def remove(self, key: int) -> None:
        code = hash(key)
        t = self.table
        if code in t:
            t.remove(code)
    def contains(self, key: int) -> bool:
        code = hash(key)
        if code in self.table:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)