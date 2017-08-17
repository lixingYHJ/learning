#!/user/bin/env python
# -*- coding: utf-8 -*-

#定义一个类

print 'define a Student'

class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

lix = Student('lix',90)
print lix.score