class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.memory = []
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.cache:
            value_of_the_key = self.cache[key]
            self.memory.remove(key)
            self.memory.append(key)
            return value_of_the_key
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.memory.remove(key)
        elif len(list(self.cache.keys())) >= self.capacity:
            key_to_remove = self.memory.pop(0)
            del self.cache[key_to_remove]
        self.cache[key] = value
        self.memory.append(key)