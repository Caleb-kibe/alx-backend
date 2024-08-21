#!/usr/bin/env python3
"""Basic cache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
        A simple caching system without a limit.
    """
    def put(self, key, item):
        """add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """gets an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
