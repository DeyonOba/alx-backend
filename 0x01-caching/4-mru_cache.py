#!/usr/bin/env python3
"""
Create a class `MRUCache` that inherits from `BaseCaching` and is a
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
            - you must discard the most recently used item
            using the (MRU algorithm).
            - you must print DISCARD: with the key discarded and following
            by a new line.
    - def get(self, key):
        - Must return the value in `self.cache_data` linked to key.
        - If key is None or if the key doesn't exist in `self.cache_data`,
        return None.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and is a caching system that
    implements [Most Recently Used] caching algorithm.
    """
    def __init__(self):
        super().__init__()
        self.cache_history = []

    def put(self, key, item):
        """
        Assigns to dictionary `self.cache_data` the item value for the
        key `key`.
        """
        if key and item:
            if key not in self.cache_history:
                self.cache_miss(key)
            else:
                self.cache_hit(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the item linked to a key, or None if key does not exist.
        """
        item = self.cache_data.get(key)

        if item is None:
            return None
        # Update the most recently used key in `self.cache_history`
        self.cache_hit(key)
        return item

    def cache_miss(self, key):
        """
        Implementing one of the two outcomes of data requested from
        a Cache.

        A cache miss occurs when the requested data is not found in the
        cache.  In this case the system has to request the data from a
        slower data store.

        For this implementation we would encounter a missed cache for
        two reasons:

        i. Capacity Limitation due to constraint `self.MAX_ITEMS`,
        here the cache has a limited memory storage.
        ii. When the cache is first intialized, it starts empty, but
        needs to be populated by the missed key.

        Args:
            key: key missed in cache.
        """
        if len(self.cache_history) == self.MAX_ITEMS:
            discarded_key = self.cache_history.pop(-1)
            self.cache_data.pop(discarded_key)
            print("DISCARD: {}".format(discarded_key))
        self.cache_history.append(key)

    def cache_hit(self, key):
        """
        Implementing one of the outcomes of data requested from a Cache.

        Cache hit occurs when the requested data is found in the cache.
        This means that the data was previously stored in the cache, allowing
        for quick retrieval without need to access a slower data store.
        Cache hit improves performance by reducing time needed to retrieve
        data.

        Args:
            key: key found in the cache.
        """
        self.cache_history.remove(key)
        self.cache_history.append(key)
