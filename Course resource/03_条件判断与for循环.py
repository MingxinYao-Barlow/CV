# -*- coding: utf-8 -*-
# 03_条件判断与for循环
# 从 Jupyter Notebook HTML 自动提取

# 条件判断 if else elif
score = int(input("请输入分数："))

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# if 嵌套
x = int(input("请输入数字："))
if x > 10:
    if x > 20:
        print("x > 20")
    else:
        print("x > 10 but not > 20")
else:
    print("x < 10")

# 商场收银员 1. 录入商品价格 2. 录入用户年龄 3. 未成年人打7折 4. 60以上人群打6折 5. 其他人群打9折 6. 输出客户需要支付多少钱
# VIP判断：0.8

price = int(input("请输入价格："))
userAge = int(input("请输入年龄："))

if userAge < 18:
    print(price * 0.7)
elif userAge > 60:
    print(price * 0.6)
else:
    print(price * 0.9)

# 商场收银员 1. 录入商品价格 2. 录入用户年龄 3. 未成年人打7折 4. 60以上人群打6折 5. 其他人群打9折 6. 输出客户需要支付多少钱
# VIP判断：0.8

price = int(input("请输入价格："))
userAge = int(input("请输入年龄："))
isVIP = input("是否为VIP：")

if userAge < 18:
    price = price * 0.7
elif userAge > 60:
    price = price * 0.6
else:
    price = price * 0.9

if isVIP == "是":
    price = price * 0.8

print(price)

# 输入一个数，判断奇数偶数，如果是奇数输出“odd number”，如果是偶数输出"even number"

num = int(input("请输入一个数："))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# 循环 for
for i in range (5):
    print(i)

for i in range (2,6):
    print(i)

customer = ["Mike", "Alex", "Luna"]
for i in customer:
    print(i)

male_count = 0
female_count = 0
customer_info = ["Male", "Female", "Male", "Male", "Female", "Male"] #列表
for i in customer_info:
    if i == "Male":
        male_count = male_count + 1
    else:
        female_count = female_count + 1

print(f"male number = {male_count}")
print(f"female number = {female_count}")

#大于100客户 - > 输出他们消费的金额
customer_expense_0922 = [125, 800, 1254, 15, 36, 756, 187, 103, 55, 67]
for i in customer_expense_0922:
    if i > 100:
        print(i)

for i in range (1,6):
    print("*" * i)

for i in range (1,6):
    print("*" * (6 - i))

for i in range (1,6):
    print(" " * (5 - i) + "*" * i)

for i in range (1,6):
    print(" " * (i - 1) + "*" * (6 - i))

for i in range (1,6):
    print(" " * (5 - i) + "*" * i + (i - 1) * "*")

for i in range (1,6):
    print(" " * (i - 1) + "*" * (6 - i) + (5 - i) * "*")
