class HashTable():
    def __init__(self):
        self._size = 29
        self._array = [[] for _ in range(self._size)]

    def hash(self, key):
        hash_key = 0
        for char in key:
            hash_key += ord(char)
        hash_key = hash_key % self._size
        return hash_key

    def __setitem__(self, key, value):
        hash_key = self.hash(key)
        for index, item in enumerate(self._array[hash_key]):
            if len(item) == 2 and item[0] == key:
                self._array[hash_key][index] = (key, value)
                return
        self._array[hash_key].append((key, value))

    def __getitem__(self, key):
        hash_key = self.hash(key)
        for item in self._array[hash_key]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def __delitem__(self, key):
        hash_key = self.hash(key)
        for index, item in enumerate(self._array[hash_key]):
            if item[0] == key:
                del self._array[hash_key][index]
                return
        raise KeyError(key)


