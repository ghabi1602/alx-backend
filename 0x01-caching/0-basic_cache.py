#!/usr/bin/env python3
"""a caching system"""
BaseCaching = __import__('base_caching') .BaseCaching


class BasicCache(BaseCaching):
    """a caching system class definition"""

    def __init__(self):
        """BasicCache instructor method"""
        super().__init__()

    def put(self, key, item):
        """adds a key/item pair into the cache_data dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns the value of the provided key from the cache_data dict"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
