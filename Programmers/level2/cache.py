from collections import deque

def updateCacheMiss(cache, city):
    cache.popleft()
    cache.append(city)
    
def updateCacheHit(cache, city):
    cache.append(city)
    cache.remove(city)
    
def solution(cacheSize, cities):
    total_t = 0
    cache = deque([])
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in cache:
            updateCacheHit(cache, city)
            total_t += 1
        elif len(cache) < cacheSize:
            cache.append(city)
            total_t += 5
        else:
            updateCacheMiss(cache, city)
            total_t += 5
    return total_t