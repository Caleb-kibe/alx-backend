#!/usr/bin/env python3
""" LFUCache module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching
        A caching system that uses LFU (Least Frequently Used) policy.
    """

    def __init__(self):
        """ Initialize the class"""
        super().__init__()
        self.frequency = {}
        self.access_order = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key is already in the cache, update the item and frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Need to remove the least frequently used item
                lfu_items = [k for k, v in self.frequency.items()
                             if v == min(self.frequency.values())]
                if len(lfu_items) > 1:
                    # If there's a tie, use LRU among the least frequently used
                    lfu_key = None
                    for k in self.access_order:
                        if k in lfu_items:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_items[0]

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.access_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new key and item to the cache
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.access_order.append(key)

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and access order
        self.frequency[key] += 1
        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data.get(key)
