#!/user/bin/env python
# -*- coding: utf-8 -*-

# 机器学习

# 绘制坐标点
import matplotlib.pyplot as plt  

x=[1,2,3,4]  
y=[5*t+4 for t in x]
z=[t**2 for t in x]  
plt.plot(x,y)  
plt.plot(x,z) 
plt.show() 

	