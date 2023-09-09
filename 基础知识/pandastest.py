# -*- codeing = utf-8 -*-
# @Time : 2023/9/2 20:05
# @Author : Yang
# @File : pandas.py
# @Software : PyCharm

import pandas as pd
import numpy as np

arr_1 = np.arange(0, 20).reshape(5, 4)
# df = pd.DataFrame(arr_1, index=['row1', 'row2', 'row3', 'row4', 'row5'], columns=['col1', 'col2', 'col3', 'cols'])
df = pd.read_csv('data/archive/train.csv')  #读取csv表格数据
df1 = df.head(5) #head 显示前五行
print(df1)