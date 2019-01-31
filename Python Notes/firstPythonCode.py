# name = input('What is your name')

# age = int(input("What is your age"))
# print(name)
# print(age + 5)

# if age >= 21:
#     print("You get free beer!")

# age = int(input("What is your age"))
# if age >= 21:
#     print("You get free beer!")
# elif age < 18:
#     print("You get nothing!")
# else:
#     print('Huh?')

# count = 0

# while count < 10:
#     count += 1
#     print("The count is %d" %(count))
# print("Done")

# answer = ' '
# while answer != 'when':
#     answer = input('Say when: ')
#     answer = answer.lower()
# print("Cheese")

# y = int(input("Where do you want to start"))
# z = int(input("Where do you want to end"))

# numbers = []
# def f(x):
#     return x+1

# for x in range(y,z):
#     numbers.append(f(x))
# print(numbers)

# from math import sqrt

# def quadratic(a, b, c):
#     x1 = -b / (2*a)
#     x2 = sqrt(b**2 - 4*a*c)/(2*a)
#     return ((x1 + x2), (x1 - x2))

# print(quadratic(33,93,62))

# a = "Hello World"

# def someFun():
#     a = "goodbye"
#     print("inside function {a}".format(a=a))

# someFun()    
# print("outside function {a}".format(a=a))

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# f_output = []
# g_output = []

# def f(x):
#     return x + 2
# def g(x):
#     return x - 3

# x_list = list(range(-3, 5))
# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))
# pyplot.plot(x_list, f_output, x_list, g_output)
# pyplot.savefig('myplot.png')
# pyplot.close() # start a new plot

# from turtle import *
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)

# mainloop()

from turtle import *

down()
pencolor('orange')
width(10)
circle(180)