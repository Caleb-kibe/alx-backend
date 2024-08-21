#!/usr/bin/env python3
"""LRUCache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching
        A caching system that uses LRU (Least Recently Used) policy.
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
                # discard the least recently used item
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """get item by key"""
        if key is None or key not in self.cache_data:
            return None
        # update the access order since this key was accessed
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data.get(key)
