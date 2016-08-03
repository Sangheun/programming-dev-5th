# def absolute(fn):
#     def wrap(*args):
#         return abs(fn(*args))
#     return wrap

def absolute(fn):
    def wrap(*args):

        # 1)
        # mylist = []
        # for i in args:
        #     mylist.append(abs(i))

        # 2)
        # mylist = [abs(i) for i in args]

        # 3)
        mylist = map(abs, args)

        return fn(*mylist)
    return wrap




@absolute
def mysum(x,y):
    return x + y

@absolute
def mysum2(x,y,z):
    return x + y + z

@absolute
def mysum3(x,y,z,a):
    return x + y + z + a


print(mysum(1,2))
print(mysum(-10,-2))
print(mysum2(-10,-1,-3))
print(mysum3(-10,-1,-3,-4))

