#!/user/bin/env python
# -*- coding: utf-8 -*-

#map和reduce的使用

#首字母大写
def format(str):
	strLen = len(str)
	firstChar = str[:1]
	otherChar = str[1:strLen]

	firstChar = firstChar.upper()
	otherChar = otherChar.lower();
	str = firstChar+otherChar

	return str

print map(format,['adam', 'LISA', 'barT'])

#用reduce实现乘法
def f(x,y):
	return x*y

def prop(list):
	return reduce(f,list)

print prop([1,2,3,4])