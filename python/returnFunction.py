#!/user/bin/env python
# -*- coding: utf-8 -*-

#返回函数
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

tmp = count()
print tmp[0];
print tmp[0]();

f1,f2,f3 = count()
print f1()