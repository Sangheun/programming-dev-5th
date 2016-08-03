import time

cached_1 = {}

def mysum(x,y):
    key = (x,y)
    if key not in cached_1:
        time.sleep(1)
        cached_1[key] = x + y
    print(cached_1)
    return cached_1[key]

print(mysum(1,2))
print(mysum(2,3))
print(mysum(3,4))
print(mysum(4,5))

cached_2 = {}

def mymultiply(x,y):
    key = (x,y)
    if key not in cached_2:
        time.sleep(1)
        cached_2[key] = x * y
    print(cached_2)
    return cached_2[key]

print(mymultiply(1,2))
print(mymultiply(2,3))
print(mymultiply(3,4))
print(mymultiply(4,5))

