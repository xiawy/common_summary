import logging
import requests


class BaseAPI(object):
    def _request(self, method, endpoint, **kwargs):
        kwargs['method'] = method

        request_url = '%s%s' % (self.get_base_url(), endpoint)
        kwargs['url'] = request_url

        self.before_request(kwargs)
        result = requests.request(**kwargs)
        if not result.ok:
            logging.error('request to %s (%s) failed: %s',
                          self.__class__.__name__, request_url, result.text)
        return result

    def get_base_url(self):
        raise NotImplementedError

    def before_request(self, kwargs):
        pass

    def get(self, endpoint, params=None, **kwargs):
        return self._request('GET', endpoint, params=params, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self._request('POST', endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self._request('PUT', endpoint, data=data, **kwargs)

    def options(self, endpoint, **kwargs):
        return self._request('OPTIONS', endpoint, **kwargs)

    def head(self, endpoint, **kwargs):
        return self._request('HEAD', endpoint, **kwargs)

    def patch(self, endpoint, data=None, **kwargs):
        return self._request('PATCH', endpoint, data=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)


class BaseServiceAPI(BaseAPI):
    def __init__(self, token=None):
        super().__init__()
        self._token = token or self.default_token()

    def get_base_url(self):
        raise NotImplementedError

    def default_token(self):
        raise NotImplementedError

    def before_request(self, kwargs):
        auth = (self._token, None)
        kwargs.setdefault('auth', auth)


class Battlefront(BaseServiceAPI):
    def default_token(self):
        return 'service.battlefront.token'

    def get_base_url(self):
        return 'service.battlefront.base_url'


#   新式类与旧式类的区别
#   1、继承搜索的顺序发生了改变,经典类多继承属性搜索顺序: 先深入继承树左侧，再返回，开始找右侧（深度优先）;
#      新式类多继承属性搜索顺序: 先水平搜索，然后再向上移动（广度优先）
#   2、新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中。
#   3、新式类对象可以直接通过__class__属性获取自身类型:type（类似于type()的结果）


#   类中几个概念：
#   1、python中一切均是对象，类型也是对象。所有类型的元类默认都是type
#   2、__new__()方法主要用来初始化时分配内存，为类的类方法，调用时还没有实例对象。可用来实现单例模式
#   3、__call__()使类的表现更像一个函数，允许被调用。常被用来实现装饰器类


