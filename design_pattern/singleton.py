from functools import wraps


# 通过 __new__() 实现单例模式
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


# 装饰器实现单例
def singleton(cls):
    _instance = {}             # 此处仅在定义函数时会运行

    @wraps(cls)
    def instance(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]
    return instance


@singleton
class A(object):
    def __init__(self, *args, **kw):
        self.a = 1


# 注: 1、__init__ 是实例方法，__new__() 是类方法
