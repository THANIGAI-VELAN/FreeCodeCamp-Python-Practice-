class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hash_index = self.hash(key)
        if hash_index not in self.collection:
            self.collection[hash_index] = {}
        self.collection[hash_index][key] = value

    def remove(self, key):
        hash_index = self.hash(key)
        if hash_index in self.collection and key in self.collection[hash_index]:
            del self.collection[hash_index][key]
           
            if not self.collection[hash_index]:
                del self.collection[hash_index]

    def lookup(self, key):
        hash_index = self.hash(key)
        if hash_index in self.collection:
            return self.collection[hash_index].get(key, None)
        return None
