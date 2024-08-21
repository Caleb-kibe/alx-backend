#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFOCache class that inherits from BaseCaching
        A caching system that uses FIFO (First In First Out) policy.
    """
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # update the order if the key already exists
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """get item by key"""
        if key is None is key not in self.cache_data:
            return None
        return self.cache_data.get(key)
