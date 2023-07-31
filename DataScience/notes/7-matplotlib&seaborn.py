# Veri Görselleştirme | matplotlib & seaborn

# matlplotlib
# kategorik değişken varsa sütun grafiği. countplot bar
# sayısal değişken varsa hist, boxplot

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

#df['sex'].value_counts().plot(kind='bar')
#plt.show()

# plt.hist(df["age"])
# plt.show()

# plt.boxplot(df["fare"])
# plt.show()

# matplotlib özellikleri

"""x = np.array([1, 8])
y = np.array([0, 150])

plt.title("Ana baslik")
plt.xlabel("X ekseni isim")
plt.ylabel("Y ekseni isim")
plt.plot(x, y)
plt.grid()
plt.show()"""

# seaborn

df1 = sns.load_dataset("tips")
df["sex"].value_counts()
sns.countplot(x=df1["sex"], data=df1)
plt.show()

sns.boxplot(x=df1["total_bill"])
plt.show()