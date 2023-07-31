# Pandas Series

import pandas as pd
import seaborn as sns

a = pd.Series([10, 77, 12, 4, 5])
print(a, type(a), "\n", a.index, a.dtype, a.size, a.ndim, a.head(2), a.tail(3))

# veri okuma
# df = pd.read_csv("{path}")

df = sns.load_dataset("titanic")
print(df.describe().T) #df.head(), df.info, df.shape, df.columns, df.index

print(df.isnull().values.any()) # veri setinde eksiklik var mı

# Pandasta seçim işlemleri

print(df.index)

print(df.drop(0, axis=0).head()) # 0. index silindi

delete_index = [1, 3, 5, 7]

print(df.drop(delete_index, axis=0).head(10)) # seçili indexler silindi
#df.drop(delete_index, axis=0, inplace=True) ile yapılan değişiklik kalıcı olarak kaydedilir

# değişkenler üzerinde işlemler

print("age" in df)
print(df[["age"]].head()) # 2 köşeli parantez ile çağırırsan dataframe olarak kalır, tek ile çağırırsan seri olarak gelir

col_names = ["age", "adult_male", "alive"]

print(df[col_names]) 