from collections import OrderedDict

#https://docs.python.org/3/library/collections.html#collections.OrderedDict
#https://pymotw.com/3/collections/ordereddict.html


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10): #set capacity
        self.cache = OrderedDict()
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.cache: # if key-value not found return None
            return None 
        else:
            self.cache.move_to_end(key) # move key-value to end to show it was most-recently used
            return self.cache[key] # return value associated with key

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        self.cache[key] = value # set key and value
        self.cache.move_to_end(key) # move key-value to the end
        if len(self.cache) > self.limit: # if cache is longer than limit
            self.cache.popitem(last = False) # remove first key-value


######LRU CACHE Notes from backtobackswe#########

# L - last
# R - Recently
# U - Used

# Cache eviction policy limits the amount of info/nodes in cache - keeping only the most 
    # items and evicting the last  if over capacity

# What Is An LRU Cache?
    # So a LRU Cache is a storage of items so that future access to those items can be 
        # serviced quickly and an LRU policy is used for cache eviction.


# The Constraints/Operations
    # Lookup of cache items must be O(1)
    # Addition to the cache must be O(1)
    # The cache should evict items using the LRU policy


my_cache = LRUCache(3)
my_cache.set('key1', 'value1')
print(my_cache.get('key1'))
print(my_cache.limit)
