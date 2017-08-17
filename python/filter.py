#!/user/bin/env python
# -*- coding: utf-8 -*-

#filter的使用

#筛选1~100内的素数
def isPrime(num):
	result = True
	if num == 1 :
		pass
	else :
		for x in xrange(2,num):
			if num % x == 0 :
				result = False

	return result

print filter(isPrime,range(1,101))