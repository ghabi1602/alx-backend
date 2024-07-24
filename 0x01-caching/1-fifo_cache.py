#!/usr/bin/env python3
"""a caching system definition"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class definition FIFOCache
        that inherits from BaseCaching
    """
    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """puts an item into the cache_data disctionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_item = list(self.cache_data.items())[0]
                key_to_remove = first_item[0]
                self.cache_data.pop(key_to_remove)
                print('DISCARD: {}'.format(key_to_remove))

    def get(self, key):
        """gets the value of a key from within the cache_data dict"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
