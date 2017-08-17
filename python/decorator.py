#!/user/bin/env python
# -*- coding: utf-8 -*-

#装饰器
import functools

def log(fun):
	@functools.wraps(fun)
	def wrapper(*arg,**kw):
		print 'start call %s'%fun.__name__
		result = fun(*arg,**kw)
		print 'end call %s'%fun.__name__
		return result
	return wrapper

@log
def now():
	print 'now'

@log
def add(x,y):
	return x+y

now()
print now.__name__
print add(2,3)

