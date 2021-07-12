#-*- coding:utf-8 -*-

class _Functor():
    def __init__(self, oFunc, *args, **kwargs):
        self._func = oFunc
        self._args = args
        self._kwargs = kwargs
        return 

    def __call__(self, *args, **kwargs):
        self._kwargs.update(kwargs)
        self._args += args
        return self._func(*self._args, **self._kwargs)

def Functor(func, *args, **kwargs):
    return _Functor(func, *args, **kwargs)
