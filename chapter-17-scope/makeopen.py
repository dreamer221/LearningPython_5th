import builtins

def makeopen(id):
    ori = builtins.open
    def custom(*kargs, **pargs):
        print('Cuntom open call %r:'%id, kargs, pargs)
        return ori(*kargs, **pargs)
    builtins.open = custom
