from tabulate import tabulate
from prettytable import PrettyTable


def cal_BMR_TDEE(gender, age, height, weight, intensity):
    if gender == '男':
        BMR = 66 + 13.7 * weight + 5 * height - 6.8 * age
    else:
        BMR = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
    TDEE_weight = [1.2, 1.375, 1.55, 1.725, 1.9]
    return round(BMR, 1), round(BMR * TDEE_weight[intensity], 1)


def format_for_print(df):
    table = PrettyTable([''] + list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    return str(table)
