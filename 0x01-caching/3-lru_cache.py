#!/usr/bin/env python3
"""caching system module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """caching system class definition"""
    checker = []

    def __init__(self):
        """the constructor method"""
        super().__init__()
        self.checker = []

    def put(self, key, item):
        """adds a key/value pair within a cache_data dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.checker:
                self.checker.remove(key)
            self.checker.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                key_to_remove = self.checker.pop(0)
                del self.cache_data[key_to_remove]
                print('DISCARD: {}'.format(key_to_remove))

    def get(self, key):
        """gets the value of a key from within a dict"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.checker:
            self.checker.remove(key)
        self.checker.append(key)
        return self.cache_data[key]
