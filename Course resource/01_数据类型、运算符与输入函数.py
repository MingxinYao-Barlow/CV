# -*- coding: utf-8 -*-
# 01_数据类型、运算符与输入函数
# 从 Jupyter Notebook HTML 自动提取

# 数据类型

x = 5 # int整数
y = 3.14 # float 浮点数
s = "hello" # string 字符串
s1 = "world"
b = True # bool布尔值 True/False

# 算数运算符：+ - * / // %
print (x + y) # 5+3.14=8.14

print (x - y) # 5-3.14=1.859999

print (x * y) # 5*3.14=15.700000000000001

x, y = 10, 3
print(x / y) # 10 / 3 = 3.333333

print(x // y) # 10 // 3 = 3

print(x % y) # 10 % 3 = 1

# 赋值运算符 
x = 10
print(x)

# +=
x += 1 #x = x + 1
print(x)

x = 10
x *= 2 #x = x * 2
print(x)

x = 10
x -= 2 #x = x - 2
print(x)

#比较运算符 ->bool
x = 5
y = 6

print(x==y)

print(x!=y)

print(x>y)
print(x>=y)

print(x<y)
print(x<=y)

#逻辑运算符 not > and > or
x = 5
print(x > 3 and x <6)

print(x > 3 or x < 4)

print(not x > 3)

#键盘输入
content = input("please enter content: ")

content = float(content)
content = content + 100
print(content)

# 小试牛刀
# 设计一个超市的打折计算程序
# 输入商品价格
# 输入折扣力度（小数）
# 输出价格

price = input("enter a price: ")
price = float(price)
print(price)

discount = input ("enter discount：")
discount = float(discount)
print(discount)

print(price * discount)

input("enter something:") # input里可以写提示功能

# 输入学生的考试成绩；输入学生的平时成绩；输入考试成绩的占比（0.5；0.6）；输出学生的总成绩

exam = input("enter the exam grade: ")
exam = float(exam)
print(exam)

attendance = input("enter the attendance grade: ")
attendance = float(attendance)
print(attendance)

percentage = input("enter the percentage (0.0): ")
percentage = float(percentage)
print(percentage)

finalGrade = exam * percentage + attendance * (1 - percentage)
print(finalGrade)
