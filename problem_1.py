from collections import OrderedDict 

class LRU_Cache: 
	def __init__(self, capacity: int): 
		self.cache = OrderedDict() 
		self.capacity = capacity 

	def get(self, key: int) -> int: 
		if key not in self.cache: 
			print(-1)
		else: 
			self.cache.move_to_end(key) 
			print(self.cache[key]) 
 
	def set(self, key: int, value: int) -> None: 
		self.cache[key] = value 
		self.cache.move_to_end(key) 
		if len(self.cache) > self.capacity: 
			self.cache.popitem(last = False) 
 

our_cache = LRU_Cache(5)#cache size 5

our_cache.get(5)#return -1
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.set(7,7)
our_cache.get(4)#return -1
