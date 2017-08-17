#!/user/bin/env python
# -*- coding: utf-8 -*-

#高阶函数
def add(x,y,f):
	return f(x) + f(y)

print add(-6,6,abs)



