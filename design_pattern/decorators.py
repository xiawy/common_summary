from functools import wraps
import logging


# 函数装饰器
def logged(level, name=None, message=None):
    def decorators(func):
        log_name = name if name else func.__module__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorators


@logged(logging.DEBUG)
def func_decor(x, y):
    return x + y


# 类装饰器
class Decorators(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('装饰器的参数：', self.name)
            result = func(*args, **kwargs)
            print('函数的参数：', *args)
            return result
        return wrapper


@Decorators('xia')
def class_decor(x, y):
    print(x + y)

# 注: 1、使用实例方法 __call__ 赋予类可执行的特性


