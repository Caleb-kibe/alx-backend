#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
        A caching system that uses MRU (Most Recently Used) policy.
    """

    def __init__(self):
        """initialize the class"""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """add an item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # update the order if the key already exists
                self.access_order.remove(key)
            self.cache_data[key] = item
            self.access_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently used item
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data.get(key)
