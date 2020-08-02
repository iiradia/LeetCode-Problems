class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        
    def add(self, key: int) -> None:
        
        if hash(key) >= len(self.set):
            self.set.extend([None for _ in range(hash(key)+2)])
            
        self.set[hash(key)] = key
        
    def remove(self, key: int) -> None:
        
        if hash(key)>=len(self.set):
            return
        self.set[hash(key)] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if hash(key)>=len(self.set):
            return False
        
        if self.set[hash(key)] is not None:
            return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)