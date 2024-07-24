#!/usr/bin/env python3
"""
Create a class `LIFOCache` that inherits from `BaseCaching` and is a
caching system:
    - You must use `self.cache_data` - dictionary from the parent
    `BaseCaching`.
    - You can overload `def __init__(self): but don't forget to call
    the parent init: `super().__init__()`
    - def put(self, key, item):
        - Must assign to the dictionary `self.cache_data` the item
        value for the key `key`.
        - If `key` or `item` is None, this method should not do anything.
        - If the number of items in `self.cache_data` is higher that
        `BaseCaching.MAX_ITEMS`:
            - you must discard the last item put in cache
            using the (LIFO algorithm).
            - you must print DISCARD: with the key discarded and following
            by a new line.
    - def get(self, key):
        - Must return the value in `self.cache_data` linked to key.
        - If key is None or if the key doesn't exist in `self.cache_data`,
        return None.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and is a caching system that
    implements FIFO caching algorithm.
    """
    def __init__(self):
        super().__init__()
        self.cache_history = []

    def put(self, key, item):
        """
        Assigns to dictionary `self.cache_data` the item value for the
        key `key`. If number of items in `self.cache_data`, then discard
        the first item put into the dictionary using the FIFO principle.
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_history:
                self.cache_history.append(key)
            else:
                self.cache_history.remove(key)
                self.cache_history.append(key)
            if len(self.cache_history) > self.MAX_ITEMS:
                discarded_key = self.cache_history.pop(-2)
                self.cache_data.pop(discarded_key)
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        Get the item linked to a key, or None if key does not exist.
        """
        item = self.cache_data.get(key)

        if item is None:
            return None
        return item
