__author__ = 'Administrator'
# from numpy import *
# from scipy.optimize import fsolve
# from math import sin,cos
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
import  os;

def KillExcel():
    ret = os.system('TASKKILL /F /IM excel.exe ')
#  os.system('taskkill /f /pid '+str(ret))


KillExcel()
#
# def pluser(a,b):
#     # print "the result of pluser is %d" % (a+b)
#     return a+b
#
# def testNumpy():
#     x = array([4,5,6])
#     print(x)
#
# def half_circle(x):
#     return (1-x**2)**0.5
#
# N = 10000
# x = linspace(-1, 1, N)
# dx = 2.0/N
# y = half_circle(x)
# print(dx*sum(y[:-1]+y[1:]))
# xcord = zeros(N)
# ycord = zeros(N)
# markers = []
# colors = []
# # for i in range(N)
#
# fig = plt.figure()
# ax = fig.add_subplot()
# plt.show()


# def f(x):
#     x0 = float(x[0])
#     x1 = float(x[1])
#     x2 = float(x[2])
#     return [
#         5*x1+3,
#         4*x0*x0 - 2*sin(x1*x2),
#         x1*x2 - 1.5
#     ]


# result = fsolve(f, [1,1,1])

#print(result)
#print(f(result))

#testNumpy();

