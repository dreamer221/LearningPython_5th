print("I'm:", __name__)

def minmax(test, *args):
    print(test.__name__, '函数', end=' ')
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y):
    return x < y

def greathan(x, y):
    return x > y

if __name__ == "__main__":
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
    print(minmax(greathan, 4, 2, 1, 5, 6, 3))