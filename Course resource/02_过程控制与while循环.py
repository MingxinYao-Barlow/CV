# -*- coding: utf-8 -*-
# 02_过程控制与while循环
# 从 Jupyter Notebook HTML 自动提取

#过程控制 break continue

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

for x in fruits:
    if x == "banana":
        break
    print(x)

for x in fruits:
    if x == "banana":
        continue
    print(x)

#调仓例子
stock_storage = [254400, 879000, 15000, 345500, 16500, 200000, 280000, 670000, 16000, 198000]
deposit = 28000000

for x in stock_storage:
    print(f"the value of item is {x}")
    deposit = deposit + x
    print(f"the current deposit value is {deposit}")
    if deposit > 30000000:
        break

# while
i = 1

while i < 5:
    print(i)
    i += 1

# 死循环

n = 10
i = 0

while i<n:
    n = n + 1
    i = i + 1
    print(i,n)

# 自动寻找100以内的所有基数

number = 0

while number < 100:
    number += 1
    if number % 2 != 0:
        print(number)

#调仓例子
stock_storage = [254400, 879000, 15000, 345500, 16500, 200000, 280000, 670000, 16000, 198000]
deposit = 28000000

for x in stock_storage:
    print(f"the value of item is {x}")
    deposit = deposit + x
    print(f"the current deposit value is {deposit}")
    if deposit > 30000000:
        break

stock_storage = [254400, 879000, 15000, 345500, 16500, 200000, 280000, 670000, 16000, 198000]
deposit = 28000000
i = 0

while deposit < 30000000:
    deposit = deposit + stock_storage[i]
    print(f"卖出{stock_storage[i]}, 余额{deposit}")
    i = i + 1

# 函数
def greeting():
    print("Hello, Ann")

greeting()

def greeting(_name):
    print(f"Hello, {_name}")

greeting("Dezheng")
greeting("Mingxin")

def add_numbers(x, y):
    print (x + y)

add_numbers(1, 2)
add_numbers(100, 208)

def add_numbers(x, y):
    return (x + y)

print(add_numbers(1, 2) + 1)

stock_storage = [254400, 879000, 15000, 345500, 16500, 200000, 280000, 670000, 16000, 198000]
deposit = 28000000
i = 0

while deposit < 30000000:
    deposit = deposit + stock_storage[i]
    print(f"卖出{stock_storage[i]}, 余额{deposit}")
    i = i + 1

def selling_stock(deposit, ideal_balance, stock_storage):
    i = 0
    while deposit < ideal_balance:
        deposit = deposit + stock_storage[i]
        print(f"卖出{stock_storage[i]}, 余额{deposit}")
        i = i + 1

selling_stock(20000000,22000000,[254400, 879000, 15000, 345500, 16500, 200000, 280000, 670000, 16000, 198000])

depo = 13000000
ideal = 13500000
sto_storage = [254400, 879000, 15000, 345500, 16500, 200000, 280000, 670000, 16000, 198000]
selling_stock(depo, ideal, sto_storage)

# 自动寻找100以内的所有基数 - 转换为函数

def find_oddnumber(x):
    number = 0
    while number < x:
        number += 1
        if number % 2 != 0:
            print(number)

find_oddnumber(128)
