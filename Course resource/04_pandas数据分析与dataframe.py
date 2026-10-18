# -*- coding: utf-8 -*-
# 04_pandas数据分析与dataframe
# 从 Jupyter Notebook HTML 自动提取

import pandas as pd

#DataFrame 多维表一列数据的转换
calories = [420, 380, 390]
df = pd.DataFrame(calories, columns = ["calories"])

df

#DataFrame 多维表多列数据的转换
data ={
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

df #调用DataFrame

df["calories"] #按照列名调用数据

df.loc["day1"] #按照行索引调用数据

df.loc["day2"]

#----------数据读取--------
pd.read_csv()
pd.read_excel()
pd.read_sql()
pd.read_json()

healthAppData = pd.read_csv("data.csv")

healthAppData

print(healthAppData["Duration"][168])

healthAppData["Duration"].describe()

healthAppData["Duration"]

count = 0
for i in healthAppData["Duration"]:
    if i > 60:
        count += 1
        print(i)
print(f"there are {count} clients whose duration lasts longer than 60 minutes")

count = 0
for i in healthAppData["Calories"]:
    if i < 300:
        count += 1
        print(i)
print(f"there are {count} clients whose calory level is smaller than 300")

healthAppData.loc[0]

print(healthAppData["Duration"].loc[healthAppData["Duration"]>60].count())

healthAppData["Duration"].loc[healthAppData["Duration"]>60]

healthAppData["Calories"].loc[healthAppData["Calories"]<300]

print(healthAppData["Calories"].loc[healthAppData["Calories"]<300].count())

# Pandas中的描述统计
.mean()
.count()
.median()
.mode()
.max()
.min()
.var()
.std()

healthAppData["Calories"].std()

healthAppData["Duration"].loc[healthAppData["Calories"]<300].mean()

healthAppData["Pulse"].loc[healthAppData["Duration"]>60].median()

healthAppData["Pulse"].loc[healthAppData["Duration"]>60]

healthAppData[["Pulse", "Duration"]].loc[healthAppData["Duration"]>60]

healthAppData[["Calories", "Maxpulse"]].loc[healthAppData["Maxpulse"]>140]

healthAppData["Calories"].loc[healthAppData["Maxpulse"]>140].median()

healthAppData[["Calories", "Maxpulse"]].loc[healthAppData["Maxpulse"]>140].Calories.median()

healthAppData.loc[healthAppData["Maxpulse"]>140].Calories.median()

healthAppData.loc[healthAppData["Maxpulse"]>140].Duration.median()

healthAppData.loc[healthAppData["Maxpulse"]>140].Pulse.median()

healthAppData[["Calories", "Maxpulse"]].loc[healthAppData["Maxpulse"]>140].Pulse.median()
