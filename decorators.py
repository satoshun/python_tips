class cached_property(object):
    def __init__(self, func):
        self.__name__ = func.__name__
        self.__module__ = func.__module__
        self.__doc__ = func.__doc__
        self.func = func

    def __get__(self, inst, objtype=None):
        if inst is None:
            return self
        val = self.func(inst)
        setattr(inst, self.__name__, val)
        return val
