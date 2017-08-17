#!/user/bin/env python
# -*- coding: utf-8 -*-

# @property 的使用

class Student(object):

	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self, value):
		if(0 < value < 100):
			self.__score = value
		else :
			raise ValueError("score must between 0~100")

lix = Student()
lix.score = 90
# lix.score = 900
print lix.score