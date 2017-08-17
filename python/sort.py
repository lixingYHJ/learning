#!/user/bin/env python
# -*- coding: utf-8 -*-

#排序

def mySort(str1,str2):
	str1 = str1.lower()
	str2 = str2.lower()

	if str1 < str2 :
		return -1
	if str1 == str2 :
		return 0
	return 1

print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'],mySort)