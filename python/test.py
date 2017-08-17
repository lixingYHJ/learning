#!/user/bin/env python
# -*- coding: utf-8 -*-

import pdb

class MachineLearning(object):
	
	def __init__(self, data):
		self.__maxStep = 1000
		self.__minStep = 0.00000000001
		self.__totalCount = 0

		self.__data = data
		self.__dl = len(data)

	# 找出最优的a和b
	def findResult(self, a=0, b=0):
		step = self.__maxStep
		a, b, sumResult = self.findB(a, b, step)
		self.printLearningResult(a, b, sumResult)
		print '本次计算一共循环',self.__totalCount,'次'
		return a, b

	# 从正增长和负增长两个方向找出最优的b
	def findB(self, a=0, b=0, step=10):	
	 	crease_a, crease_b, crease_sumResult = self.creaseB(a, b, step)
		decrease_a, decrease_b, decrease_sumResult = self.creaseB(a, b, -step)

		if(crease_sumResult <= decrease_sumResult):
			a, b, sumResult = crease_a, crease_b, crease_sumResult
		else :
			a, b, sumResult = decrease_a, decrease_b, decrease_sumResult
	 	return a, b, sumResult

	# 从正增长和负增长两个方向找出最优的a
	def findA(self, a=0, b=0, step=10):	
	 	crease_a, crease_b, crease_sumResult = self.creaseA(a, b, step)
		decrease_a, decrease_b, decrease_sumResult = self.creaseA(a, b, -step)

		if(crease_sumResult <= decrease_sumResult):
			a, b, sumResult = crease_a, crease_b, crease_sumResult
		else :
			a, b, sumResult = decrease_a, decrease_b, decrease_sumResult
	 	return a, b, sumResult

	# 当学习时，按步长增长a
	def creaseA(self, a, b, step):
		learning = True
		tmp = -1
		count = 0
		while learning:
			# 统计总计算次数
			self.__totalCount += 1

			# 计算当前a，b值下，线与各点的距离
			sumResult = self.caculate(a, b)
			print 'a:', a,' sumResult:',sumResult

			# 判断是否需要继续学习
			learning = self.continueLearning(sumResult, tmp)

			if learning:
				a += step
				tmp = sumResult
			elif abs(step) > self.__minStep:
				learning = True
				if(count>2):
					a = a - 2*step
				else:
					a = a - step
				tmp = self.caculate(a,b)
				step = step/10.0
				a = a + step

			count += 1
		# 补偿a
		a = a - step
		# 打印学习过程
		self.printLearningProcess(a, b, tmp, step)
		return a,b,tmp

	# 当学习时，按步长增长b
	def creaseB(self, a, b, step):
		learning = True
		tmp = -1
		count = 0
		bList = []
		tmpList = []

		while learning:
			tmpList.append(tmp)
			bList.append(b)

			a, b, sumResult = self.findA(a, b, step)
			
			# 判断是否需要继续学习
			learning = self.continueLearning(sumResult, tmp)

			if(learning):
				b += step
				tmp = sumResult
				count += 1
			elif abs(step) > self.__minStep:
				learning = True

				# 如果连续进行了两次以上的学习，出现f(x-step)>f(x),f(x+step)>f(x)的情况
				# 将步长减少十倍，从x-step处重新寻找最优解
				# 如果只进行了一次学习，出现 f(x)<f(x+step)的情况
				# 将步长减少十倍，从x处重新寻找最优解
				if(count>2):
					# 连续调用两次pop返回到b = b - 2*step的状态
					bList.pop()
					bList.pop()

					b = bList[-1]
					tmp = tmpList[-2]
				else:
					# 返回到b = b - step的状态
					bList.pop()

					b = bList[-1]
					tmp = tmpList[-1]

				step = step/10.0
				b = b + step
				count = 1

		# 补偿b
		b = b - step
		# 打印学习过程
		# self.printLearningProcess(a, b, tmp, step)
		return a,b,tmp

	# 判断是否需要继续学习
	def continueLearning(self, currentResult, formerResult=-1):
		if(formerResult == -1 or currentResult < formerResult):
			return True
		else:
			return False

	# 打印学习过程
	def printLearningProcess(self, a, b, sumResult, step=10):
		print '当前步长为：' + str(step)
		print '最优a为：' + str(a)
		print '最优b为：' + str(b)
		print '最优距离平方和为：' + str(sumResult)
		print ''
		print '--------------------------------------------------------------------------'

	# 打印学习结果
	def printLearningResult(self, a, b, sumResult):
		print '最优a为：' + str(a)
		print '最优b为：' + str(b)
		print '最优距离平方和为：' + str(sumResult)
		print ''
		print '--------------------------------------------------------------------------'

	# 计算当前a，b值下，线与各点的距离
	def caculate(self, a, b):
		data = self.__data
		dl = self.__dl
		sumResult = 0

		for x,y in data:
			fx = a*x + b
			sumResult += (y - fx) * (y-fx)
		sumResult = abs(sumResult/dl)

		return sumResult


#绘图
import matplotlib.pyplot as plt 

class Draw(object):

	def __init__(self):
		pass

	def addLine(self, xList, yList, type='', color='red'):
		plt.plot(xList,yList,type,color=color,linewidth=2)

	def drawLines(self):
		plt.xlabel("x")
		plt.ylabel("y")

		plt.show()

	# 绘制图例
	def legend(self,plots,decs,position='best',numpoints=1):
		plt.legend(plots, decs, position, numpoints=numpoints)

import random
import math

def buildData():
	data = []
	for x in xrange(1,50):
		# y = random.randint(0,10)
		# y = math.sin(x)
		# y = math.tan(x)
		y = random.randint(0,10) + x

		item = (x,y)
		data.append(item)
	return data

def test():

	data = [(1,2),(3,4),(5,6),(6,7),(7,8),(8,9),(9,10)]
	# data = [(1,2),(2,1),(2,3),(3,2),(3,4),(4,3)]	
	# data = [(2,1),(4,3),(30,67),(90,987),(1000,37),(78,78),(66,90),(54,23),(12,4),(66,78)]
	# data = sorted(data)

	# data = buildData()

	machine = MachineLearning(data)
	a,b = machine.findResult(a=0.9, b=0)

	xList = []
	yList = []
	lineList = []

	for x,y in data:
		xList.append(x);
		yList.append(y);
		lineList.append(a*x+b)
		
	d = Draw()
	line1 = d.addLine(xList, yList, 'o')
	line2 = d.addLine(xList, lineList, color='blue')
	d.legend([line1,line2],('points', 'resultLine'))
	d.drawLines()

test()
