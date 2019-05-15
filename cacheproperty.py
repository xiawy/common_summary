
class CachedProperty(object):
    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__[self.func.__name__] = self.func(instance)
        return value


class SlowClass(object):
    @CachedProperty
    def very_slow(self):
        return 'I am property'


