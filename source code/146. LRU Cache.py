class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.remain_capacity = capacity
        self.capacity = capacity
        self.timestamp = 0
        self.order = []

    def get(self, key: int) -> int:
        if key in self.store:
            self._refresh(key, self.store[key][0])
            return self.store[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self._refresh(key, value)
        else:
            if self.remain_capacity > 0:
                self._refresh(key, value)
                self.remain_capacity -= 1
            else:
                del_key = self._get_least_used_key()
                self.store.pop(del_key)
                self._refresh(key, value)


    def _refresh(self, key, value):
        self.timestamp += 1
        if self.timestamp > 10 ** 5:
            self.timestamp = 0
        self.store[key] = (value, self.timestamp)
        self.order.append((key, self.timestamp))

    def _get_least_used_key(self):
        res = 0
        for idx, (key, timestamp) in enumerate(self.order):
            if timestamp == self.store[key][1]:
                res = key
                break
        self.order = self.order[idx+1:]
        return res


if __name__ == '__main__':
    cache = LRUCache(2);
    cache.put(1, 1)
    print(cache.store, cache.order)
    cache.put(2, 2)
    print(cache.store, cache.order)
    cache.get(1)
    print(cache.store, cache.order)
    cache.put(3, 3)
    print(cache.store, cache.order)
    cache.get(2)
    print(cache.store, cache.order)
    cache.put(4, 4)
    print(cache.store, cache.order)
    cache.get(1)
    print(cache.store, cache.order)
    cache.get(3)
    print(cache.store, cache.order)
    cache.get(4)
    print(cache.store, cache.order)