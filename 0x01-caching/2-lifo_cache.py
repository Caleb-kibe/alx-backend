#!/usr/bin/env python3
"""LIFO cache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
        A caching system that uses LIFO (Last In First Out) policy.
    """

    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # discarf the last item added
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            # update the last key to the current one
            self.last_key = key

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
