def cache(func):
    c = {}
    cache_hits = 0

    def wrapper(*args):
        key = (*args,)
        val = c.get(key)
        if val:
            cache_hits += 1
            return val
        result = func(*args)
        c[key] = result
        return result

    return wrapper
