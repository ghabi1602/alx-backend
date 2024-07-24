#!/usr/bin/env python3
"""caching system module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """caching system class definition"""
    def __init__(self):
        """the constructor method"""
        super().__init__()

    def put(self, key, item):
        """adds a key/value pair within a cache_data dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                last_item = self.cache_data.popitem()
                last_key = last_item[0]
                print('DISCARD: {}'.format(last_key))

    def get(self, key):
        """gets the value of a key from within a dict"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
