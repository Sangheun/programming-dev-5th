import time

def memoize(fn):
    cached = {}
    def wrap(x,y):
        key = (x,y)
        if key not in cached:
            cached[key] = fn(x,y)
        return cached[key]
    return wrap