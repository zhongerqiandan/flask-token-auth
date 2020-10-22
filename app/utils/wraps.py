# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 7:27 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

import time
from functools import wraps
from .generate_response import success

def func_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        if isinstance(r, dict):
            duration = time.time() - start
            r['time_consume'] = duration
            return success(r)
        return r
    return wrap
