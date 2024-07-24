#!/usr/bin/env python3
"""
Module contains a class `BasicCache` that inherits from `BaseCaching` and
is a caching system.

    - You must use `self.cache_data` - dictionary from the parent class
    `BaseCaching`
    - This caching system doesn't have limit.
    - `def `put(self, key, item):`
        - Must assign to the dictionary `self.cache_data` the `item` value
        for the key `key`.
        - If `key` or `item` is None, this method should not do anything.
    - `def get(self, key):`
        - Must return the value in `self.cache_data` linked to `key`.
        - If `key` is None or if the key doesn't exist in `self.cache_data`,
        return None.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class that inherits from `BaseCaching` and is a caching system.

    Class implements the `put` and `get` methods.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Assigns to dictionary `self.cache_data` the item value for the
        key `key`.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the item linked to a key, or None if key does not exist.
        """
        item = self.cache_data.get(key)

        if not item:
            return None
        return item
