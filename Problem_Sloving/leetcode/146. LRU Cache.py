
class LRUCache(object):            

    class CacheItem:
        
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = self
            self.next = self

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.cacheList = None
        self.rear = None
        self.tail = None
        
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.get(key):
            target = self.cache[key]
            target.prev.next = target.next            
            target.next.prev = target.prev
            self.rear.prev = target
            self.rear, self.rear.prev.next = self.rear.prev, self.rear
            if target.key == self.tail.key:
                self.tail = target.prev
            
            return target.value

        else:
            return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        cache_size = len(self.cache)
        if self.cache.get(key):
            target = self.cache[key]
            target.value = value
            target.prev.next = target.next
            target.next.prev = target.prev
            self.rear.prev = target
            self.rear, self.rear.prev.next = self.rear.prev, self.rear
            if target.key == self.tail.key:
                self.tail = target.prev

        else:
            if cache_size == 0:
                self.cache[key] = self.CacheItem(key, value)
                self.cacheList = self.cache[key]
                self.rear = self.cacheList
                self.tail = self.cacheList

            elif cache_size < self.capacity:
                self.cache[key] = self.CacheItem(key, value)
                self.rear.prev = self.cache[key]
                self.rear, self.rear.prev.next = self.rear.prev, self.rear
                self.rear.prev = self.rear
            
            elif cache_size == self.capacity:
                del(self.cache[self.tail.key])
                self.cache[key] = self.CacheItem(key, value)
                self.rear.prev = self.cache[key]
                self.rear, self.rear.prev.next = self.rear.prev, self.rear
                self.rear.prev = self.rear
                self.tail = self.tail.prev
                self.tail.next = self.tail
        
          
def test(values):
    cache = LRUCache( values[0][0] )
    for i in range(1,len(values)):
        print(i, values[i], cache.cache.keys())
        if len(values[i]) == 1:
            print(cache.get(values[i][0]))
        elif len(values[i]) == 2:
            print(cache.put(values[i][0], values[i][1]))

test([[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]])

"""
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.put(3, 3))
print(cache.put(4, 4))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(4))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(3))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(2))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(1))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.put(5, 5))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(1))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(2))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(3))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(4))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
print(cache.get(5))
print(cache.cache.keys(), cache.rear.key, cache.tail.key)
"""