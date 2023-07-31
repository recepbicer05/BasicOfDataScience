# iloc (integer base selection) & loc (label base selection)

import pandas as pd
import numpy as np
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
#print(df.head())

"""print(df.iloc[0:3, 0:3]) # 3e kadar
print(df.loc[0:3, "age"]) # 3 dahil

col_names = ["age", "embarked", "alive"]

print(df.loc[0:2, col_names])"""

# Conditional Selection

"""a = df[df["age"] > 50].head()
print(a, "\n", df[df["age"] > 50]["age"].count())

print(df.loc[(df["age"] > 50) & ((df["sex"] == "male")), ["age", "class"]].head()) # | sembolü ya da için kullanılır"""

# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# count(), first(), last(), mean(), median(), min(), max(), std(), var(), sum()

"""print(df["age"].mean())
print(df.groupby("sex")["age"].mean())
print(df.groupby("sex").agg({"age":["mean", "sum"]}))"""

#print(df.pivot_table("survived", "sex", "embarked"))    # pivot_table mean verir

# Apply and Lambda

"""df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

# apply lambda ile yapalım

print(df[["age", "age2", "age3"]].apply(lambda x: x/10).head())
#veya
print(df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head())"""

# birleştirme işlemleri

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])

df2 = df1 + 99

print(pd.concat([df1, df2], ignore_index=True))

# merge ile birleştirme işlemleri pd.merge(df1, df2) gibi birleştirilebilir




