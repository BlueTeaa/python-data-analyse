# -*- codeing = utf-8 -*-
# @Time : 2023/9/7 9:21
# @Author : Yang
# @File : Univariate_Bivariate_MultAnalysis.py
# @Software : PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("iris")

df_virginica = df.loc[df["species"] == "virginica"]
sns.distplot(df_virginica["sepal_length"])

plt.show()
# print(df.head())