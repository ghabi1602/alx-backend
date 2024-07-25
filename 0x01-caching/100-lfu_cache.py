#!/usr/bin/env python3
"""caching system module definition"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """a caching system class definition"""
    def __init__(self):
        super().__init__()
        self.rank = []

    def put(self, key, item):
        """adds an item into the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        exist = False
        for tp in self.rank:
            if key == tp[0]:
                exist = True
                break
        if exist:
            for i, tup in enumerate(self.rank):
                if key == tup[0]:
                    self.rank[i] = (tup[0], tup[1] + 1)
                    break
        else:
            self.rank.append((key, 0))

        if len(self.cache_data) > self.MAX_ITEMS:
            aux = aux = min(self.rank, key=lambda x: x[1])
            
            self.rank.remove(aux)
            del self.cache_data[aux[0]]
            print('DISCARD: {}'.format(aux[0]))

    def get(self, key):
        """gets the value of key from within cache_data dictionary"""
        if key is None or key not in self.cache_data:
            return None
        for i, tup in enumerate(self.rank):
            if key == tup[0]:
                self.rank[i] = (tup[0], tup[1] + 1)
                break
        return self.cache_data[key]
