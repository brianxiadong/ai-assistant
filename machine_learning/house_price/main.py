import matplotlib_inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import  display
matplotlib_inline.backend_inline.set_matplotlib_formats()

data = pd.read_csv('D://work//machine-learning//data20201205//Data20201205//kaggle_house_price//train.csv')

null_sum = data.isnull().sum()
print(data.columns[null_sum > len(data) * 0.7])
#清洗无效列 inplace默认false，如果false会复制一个新的出来，否则直接在老的数据对象处理
data.drop(columns=data.columns[null_sum > (len(data) * 0.7)],inplace=True)
currency = ['SalePrice']
for c in currency :
    data[c] = data[c].astype(float)

print(data.dtypes)
print(data.shape)
print(data.head())
print(data.describe())

ax = sns.histplot(np.log10(data['SalePrice']))
ax.set_xlim([3,8])
ax.set_xticks(range(4,7))
ax.set_xticklabels(['10^'+str(i) for i in range(4,7)])

plt.show()
