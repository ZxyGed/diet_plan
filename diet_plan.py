import pandas as pd
from utils import cal_BMR_TDEE, format_for_print


# 内胚型：Endomorphy； 外胚型：Ectomorph
# 内胚型：喝水都长肉，外胚型：瘦啊，太瘦啦
type = '内胚型'
weight = 66
name = 'GED'
gender = '男'
age = 23
height = 171
# [0] 久坐不动 [1] 每周低强度1-3天 [2] 每周中强度3-5天
# [3] 每周高强度6-7天 [4] 劳动密集工作或每天高强度训练
intensity = 2
# 留出的计划摄入与每日消耗的热量差
# 例如每日消耗为2500kcal，gap为500kcal，意味着你计划每日摄入2000kcal
gap = 500


# args顺序为carbon, fat, protein
if type == '外胚型':
    # 外胚型的脂肪为0.8-1.2，蛋白需要根据训练水平测定，初级0.8-1，中高级1.2-1.5
    args = [3, 1.1, 0.9]
elif type == '内胚型':
    # 蛋白需要根据训练水平测定，初级0.8-1，中高级1.2-1.5
    args = [2, 0.8, 0.9]
else:
    print("请选择正确的胚型")

# 碳水，脂肪占比
high_carbon_day_portion = [0.5, 0.15]
low_carbon_day_portion = [0.15, 0.5]
mid_carbon_day_portion = [0.35, 0.35]

total_weight = [weight * ele * 7 for ele in args]
high_carbon_day = []
mid_carbon_day = []
low_carbon_day = []

for i in range(2):
    high_carbon_day.append(total_weight[i] * high_carbon_day_portion[i] / 2)
    low_carbon_day.append(total_weight[i] * low_carbon_day_portion[i] / 2)
    mid_carbon_day.append(total_weight[i] * mid_carbon_day_portion[i] / 3)

df = pd.DataFrame([high_carbon_day, low_carbon_day, mid_carbon_day]).T
df.loc[2] = [weight * args[2]] * 3  # add protein row
df.loc[3] = df.loc[0] * 4 + df.loc[1] * 4 + df.loc[2] * 9

BMR, TDEE = cal_BMR_TDEE(gender, age, height, weight, intensity)
df.loc[4] = TDEE - gap - df.loc[3]

df = df.round(1)
df.index = ['碳水(g)', '脂肪(g)', '蛋白质(g)', '热量(kcal)', '缺口(kcal)']
df.columns = ['高碳日（2天）', '低碳日（2天）', '中碳日（3天）']

# print(tabulate(df, headers=df.columns, tablefmt='pysql'))


print('\n\n')
print(f'姓名：{name}')
print(f'(基础代谢) BMR: {BMR}kcal\t(每日消耗) TDEE: {TDEE}kcal')
# print(f'(每日消耗) TDEE: {TDEE}')
print(format_for_print(df))
print(f'PS：预留{gap}kcal空窗用于减脂，用蔬菜补足热量缺口')
print('\n')
