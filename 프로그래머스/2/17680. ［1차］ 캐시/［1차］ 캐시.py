from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize) 
    cities = [city.lower() for city in cities]
    
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            # cache hit
            if city in cache: 
                answer += 1
                cache.remove(city)
            # cache miss
            else: 
                answer += 5
        
            cache.append(city)
    return answer